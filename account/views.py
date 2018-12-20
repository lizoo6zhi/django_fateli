from django.shortcuts import render
from django.http.response import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect
from .forms import RegisterForm,UserProfileForm
import re

from django.contrib.auth.models import User
from django.contrib.auth import logout, login,views as auth_views
from django.views import View

# Create your views here.
def RegisterView(request):
    registerform = RegisterForm(request.POST)
    userprofileform = UserProfileForm(request.POST)
    if request.method == 'GET':
        return render(request, 'register.html', {"registerform":registerform, 'userprofileform':userprofileform})
    elif request.method == 'POST':
        if registerform.is_valid()*userprofileform.is_valid():
            newuser=registerform.save(commit=False)
            newuser.set_password(registerform.cleaned_data['confirm_password'])
            newuser.save()
            userprofile = userprofileform.save(commit=False)
            userprofile.user = newuser
            userprofile.save()
            data = registerform.cleaned_data
            format_string = 'username:{username}<br/>password:{password}<br/>confirmpassword:{confirm_password}'.format(**data)
            print('format_string:', format_string)
            return HttpResponse(format_string)
        else:
            return render(request, 'register.html', {"registerform":registerform, 'userprofileform':userprofileform})

from django.urls.base import reverse

#使用django自带的LoginView
class LoginViewEx(auth_views.LoginView):
    template_name = 'login.html'
    def get(self, request, *args, **kwargs):
        """Handle GET requests: instantiate a blank version of the form."""
        return self.render_to_response(self.get_context_data())

    def post(self, request, *args, **kwargs):
        """
        Handle POST requests: instantiate a form instance with the passed
        POST variables and then check if it's valid.
        """
        form = self.get_form()
        if form.is_valid():
            login(self.request, form.get_user())
            return HttpResponseRedirect(reverse('blog:blog_titles'))
        else:
            return redirect('/account/login/')

from django.contrib.auth.decorators import login_required
@login_required
def logoutex(request):
    logout(request)
    return redirect('/blog/')