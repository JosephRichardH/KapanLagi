from django.urls import path
from . import views

urlpatterns = [
    path('', views.LaguPost, name='home'),
    #path('barang/<int:toko_id>', views.LaguDetail, name='lagu_detail'),
]