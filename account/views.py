from django.shortcuts import render
from django.http.response import HttpResponse
from django.shortcuts import render
from .forms import RegisterForm,UserProfileForm
import re

from django.contrib.auth.models import User
from django.contrib.auth import views as auth_views

# Create your views here.
def register_by_forms(request):
    registerform = RegisterForm(request.POST)
    userprofileform = UserProfileForm(request.POST)
    print('USer:',User.objects.all())
    print('User:', User.objects.filter(username='zhanglin').delete())
    print('USer:',User.objects.all())
    if request.method == 'GET':
        return render(request, 'register.html', {"registerform":registerform, 'userprofileform':userprofileform})
    elif request.method == 'POST':
        if registerform.is_valid() and userprofileform.is_valid():
            newuser=registerform.save(commit=False)
            newuser.set_password(registerform.cleaned_data['password2'])
            newuser.save()
            userprofile = userprofileform.save(commit=False)
            userprofile.user = newuser
            userprofile.save()
            data = registerform.cleaned_data
            format_string = 'username:{username}<br/>password:{password1}<br/>confirmpassword:{password2}'.format(**data)
            return HttpResponse(format_string)
        else:
            return render(request, 'register.html', {"registerform":registerform, 'userprofileform':userprofileform})


class LoginViewEx(auth_views.LoginView):
    def form_valid(self, form):
        """Security check complete. Log the user in."""
        auth_views.auth_login(self.request, form.get_user())
        return HttpResponse('login access')