from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

#clase que maneja los datos para las publicaciones del Blog

class Bike(models.Model):
    id=models.CharField(max_length=255, primary_key=True)
    image = models.ImageField(upload_to="bike_img", blank=True, null=True)
    dateTime=models.DateTimeField(auto_now_add=True)
    #devuelve el autor y el titulo del blog
    def __str__(self):
        return str(self.id) + " id de la bicicleta: " + self.id
    #devuelve la direccion del blog
    def get_absolute_url(self):
        return reverse('bikes')
