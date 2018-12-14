from django.conf.urls import url
from account import views
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
urlpatterns = [
    url(r'^register/',views.register_by_forms),
    url(r'^login/', views.LoginViewEx.as_view(), name='login'),
    url(r'^profile/',views.register_by_forms),
    url(r'^password-change/$', auth_views.PasswordChangeView.as_view(), name='password_change')
]