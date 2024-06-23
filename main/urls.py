from django.urls import path
from . import views


urlpatterns = [
#   inicio

    path('', views.inicio, name='inicio'),#marca la pagina de inicio
    path('incio/', views.inicio, name='inicio'),
#bike
    path("bike_list/", views.bike_list, name="bike_list"),
    path('bike_create/create/', views.bike_create, name='bike_create'),
    path('bike_update/<int:pk>/edit/', views.bike_update, name='bike_update'),
    path('bike_delete/<int:pk>/delete/', views.bike_delete, name='bike_delete'),
    
#stations  
    path('stations_list/', views.station_list, name='station_list'),
    path('stations_create/create/', views.station_create, name='station_create'),
    path('stations_update/<int:pk>/edit/', views.station_update, name='station_update'),
    path('stations_delete/<int:pk>/delete/', views.station_delete, name='station_delete'),
]
