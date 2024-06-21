from django.urls import path
from . import views


urlpatterns = [
#   inicio

    path('', views.inicio, name='inicio'),#marca la pagina de inicio
    path('incio/', views.inicio, name='inicio'),
#bike
    path("bike/", views.bike, name="bike"),
    path('bike/create/', views.bike_create, name='bike_create'),
]
