from django.urls import path
from . import views
from django.conf.urls import url
from Home import views as views1

urlpatterns = [
    path('', views.Tampilan_Home, name='home'),
    path('input/', views.Lagu_Input, name='Lagu_Input'),
    path('signup/', views.Lagu_SignUp, name='LaguSignUp'),
    path('signin/', views.Lagu_SignIn, name='LaguSignIn'),
    path('signout/', views.Lagu_Signout, name='LaguSignOut'),
    path('lirik/', views.LirikLagu, name='lirik'),
    path('print/<int:lagu_id>', views.PrintDetail, name='print'),
    path('lirik/<int:lagu_id>', views.LaguDetail, name='LaguDetail'),
]