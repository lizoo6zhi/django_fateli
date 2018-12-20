from django.http.response import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect
from .forms import RegisterForm,UserProfileForm,My_Information_Form,UserForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import logout, login,views as auth_views
from django.urls.base import reverse
from django.views import View
from .models import UserProfile,My_Formation
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
            #data = registerform.cleaned_data
            #format_string = 'username:{username}<br/>password:{password}<br/>confirmpassword:{confirm_password}'.format(**data)
            return redirect(reverse('account:login'))
        else:
            return render(request, 'register.html', {"registerform":registerform, 'userprofileform':userprofileform})

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

@login_required
def logoutex(request):
    logout(request)
    return redirect('/blog/')


class PasswordChangeDoneViewEx(auth_views.PasswordChangeDoneView):
    def __init__(self):
        self.user = User

    @login_required
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        """Handle GET requests: instantiate a blank version of the form."""
        return HttpResponseRedirect(reverse('blog:blog_titles'))

def CreateUser(new_user):
    if not UserProfile.objects.filter(user=new_user):
        userprofile_obj= UserProfile(user=new_user)
        userprofile_obj.save()
    if not My_Formation.objects.filter(user=new_user):
        my_formation_obj= My_Formation(user=new_user)
        my_formation_obj.save()

@login_required
def Edit_My_Infomation(request):
    CreateUser(request.user)
    current_user = User.objects.get(username=request.user.username)
    userProfile = UserProfile.objects.get(user=request.user)
    my_formation = My_Formation.objects.get(user=request.user)

    if request.method == "GET":
        user_form = UserForm(instance=request.user)
        userprofile_form = UserProfileForm(initial={"birday":userProfile.birday,"phone":userProfile.phone})
        my_formation_form = My_Information_Form(initial={"school":my_formation.school, 
                                                        "company":my_formation.company,
                                                        "profession":my_formation.profession})
        return render(request, 'edit_my_information.html',{"user_form":user_form, "userprofile_form":userprofile_form, "my_formation_form":my_formation_form})
    else:
        user_form = UserForm(request.POST)
        userprofile_form = UserProfileForm(request.POST)
        my_formation_form = My_Information_Form(request.POST)
        if user_form.is_valid() * userprofile_form.is_valid() * my_formation_form.is_valid():
            user_cd = user_form.cleaned_data
            profile_cd = userprofile_form.cleaned_data
            formation_cd = my_formation_form.cleaned_data
            print('email:',user_cd['email'])
            current_user.email = user_cd['email']
            userProfile.birday = profile_cd['birday']
            userProfile.phone = profile_cd['phone']
            my_formation.school = formation_cd['school']
            my_formation.company = formation_cd['company']
            my_formation.profession = formation_cd['profession']
            print("userProfile:",userProfile)
            current_user.save()
            userProfile.save()
            my_formation.save()
        return HttpResponseRedirect(reverse('account:show_my_information'))

@login_required
def Show_My_Infomation(request):
    if request.method == 'GET':
        CreateUser(request.user)
        userProfile = UserProfile.objects.get(user=request.user)
        my_formation = My_Formation.objects.get(user=request.user)
        return render(request, 'show_my_information.html',{"user_form":request.user, "userprofile_form":userProfile, "my_formation_form":my_formation})
    else:
        return HttpResponse("ok")
