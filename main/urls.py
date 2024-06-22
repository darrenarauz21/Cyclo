from django.urls import path
from . import views


urlpatterns = [
#   inicio

    path('', views.inicio, name='inicio'),#marca la pagina de inicio
    path('incio/', views.inicio, name='inicio'),
#bike
    path("bike_list/", views.bike_list, name="bike_list"),
    path('bike/create/', views.bike_create, name='bike_create'),
    path('bikes/<int:pk>/edit/', views.bike_update, name='bike_update'),
    path('bikes/<int:pk>/delete/', views.bike_delete, name='bike_delete'),
    
#stations  
    path('stations/', views.station_list, name='station_list'),
    path('stations/<int:pk>/', views.station_detail, name='station_detail'),
    path('stations/new/', views.station_create, name='station_create'),
    path('stations/<int:pk>/edit/', views.station_update, name='station_update'),
    path('stations/<int:pk>/delete/', views.station_delete, name='station_delete'),
]
