from django.conf.urls import url
from account import views
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
urlpatterns = [
    url(r'register/',views.RegisterView, name='register'),
    url(r'login/', views.LoginViewEx.as_view(), name='login'),
    url(r'logout/', views.logoutex, name='logout'),
    url(r'profile/',views.RegisterView),
    url(r'password_change/', auth_views.PasswordChangeView.as_view(success_url='/account/password_change_done'), name='password_change'),
    url(r'^password_change_done/', views.PasswordChangeDoneViewEx.as_view(), name='password_change_done'),
]
