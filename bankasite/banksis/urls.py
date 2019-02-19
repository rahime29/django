from django.urls import path
from . import views

urlpatterns = [
    path('musteriler/' , views.musteri_list, name= 'musteri_list'),
    
]