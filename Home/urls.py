from django.urls import path
from . import views
from django.conf.urls import url
from Home import views as views1

urlpatterns = [
    path('', views.Lagu_Post, name='home'),
    path('input/', views.Lagu_Input, name='Lagu_Input'),
    path('signup/', views.Lagu_Signup, name='LaguSignUp'),
    path('signin/', views.Lagu_Signin, name='LaguSignIn'),
    path('signout/', views.Lagu_Signout, name='LaguSignOut'),
    path('lirik/', views.LirikLagu, name='lirik'),
    path('print/<int:lagu_id>', views.PrintDetail, name='print'),
    path('lirik/<int:lagu_id>', views.LaguDetail, name='LaguDetail'),
]