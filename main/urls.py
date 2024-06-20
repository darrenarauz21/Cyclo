from django.urls import path
from . import views


urlpatterns = [
#   inicio

    path('', views.inicio, name='inicio'),#marca la pagina de inicio
    path('incio/<str:slug>/', views.inicio, name='inicio'),
]