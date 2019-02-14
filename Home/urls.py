from django.urls import path
from . import views

urlpatterns = [
    path('', views.tampilan_toko, name='home'),
    path('barang/<int:toko_id>', views.toko_detail, name='toko_detail'),
]