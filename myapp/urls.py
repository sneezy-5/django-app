from django.urls import path
from . import views

urlpatterns = [
    path('', views.acceuil, name='acceuil'),
    path('quisommenous', views.indexx, name='quisommenous'),
    path('NosActivite',views.activite, name='NosActivite'),
    path('Contacter',views.contacte, name='Contacter'),
]
