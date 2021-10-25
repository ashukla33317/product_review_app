from django.urls import path
from . import views

urlpatterns=[
    path('',views.HomePage.as_view(),name="home"),
    path('login',views.LoginUser.as_view(),name="login"),
    path('signup',views.SignupUser.as_view(),name="signup"),
    path('logout',views.LogoutUser.as_view(),name="logout")
]