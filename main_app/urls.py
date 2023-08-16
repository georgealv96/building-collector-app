from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('buildings/', views.buildings_index, name='index'),
    path('buildings/<int:building_id>/', views.buildings_detail, name='detail'),
    path('buildings/create/', views.BuildingCreate.as_view(), name='buildings_create'),
    path('buildings/<int:pk>/update/', views.BuildingUpdate.as_view(), name='buildings_update'),
    path('buildings/<int:pk>/delete/', views.BuildingDelete.as_view(), name='buildings_delete'),
    path('buildings/<int:building_id>/add_visit/', views.add_visit, name='add_visit'),
    path('references/', views.ReferenceList.as_view(), name='references_index'),
    path('references/create/', views.ReferenceCreate.as_view(), name='references_create'),
]