from django.conf.urls import url
from . import views as acc_views

urlpatterns=[
    url('^register/',acc_views.UserRegister.as_view(),name='register'),
    url('^login/',acc_views.UserLogin.as_view(),name='login'),
    url('^resetpassword',acc_views.UserResetPassword.as_view(),name='resetpassword'),
    url('^editprofile/',acc_views.UserEditProfile.as_view(),name='editprofile'),
    url('^viewprofile/',acc_views.UserViewProfile.as_view(),name='viewprofile'),
]
