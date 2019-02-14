from django.urls import path
from . import views

urlpatterns = [
    path('', views.LaguPost, name='home'),
    path('lirik/', views.LirikLagu, name='lirik'),
    path('print/<int:lagu_id>', views.PrintDetail, name='print'),
    path('detail/<int:lagu_id>', views.LaguDetail, name='lagu_detail'),
]