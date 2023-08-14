from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('buildings/', views.buildings_index, name='index'),
    path('buildings/<int:building_id>/', views.buildings_detail, name='detail'),
]