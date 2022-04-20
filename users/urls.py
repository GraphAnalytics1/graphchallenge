from django.urls import path

from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('logout/', views.logoutuser, name='logoutuser'),
    path('login/', views.loginPage, name='loginpage'),
    path('home/', views.homePage, name='homepage'),
]