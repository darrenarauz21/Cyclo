from django.db import models


#para establecer las bicicletas
class Bike(models.Model):
    STATE_CHOICES = [
        ('DISPONIBLE', 'Disponible'),
        ('OCUPADO', 'Ocupado'),
        ('FUERA_DE_SERVICIO', 'Fuera de Servicio'),
    ]
    state = models.CharField(max_length=20, choices=STATE_CHOICES, default='DISPONIBLE')
    
    def __str__(self):
        return f'Bicicleta ID: {self.pk}, Estado: {self.state}'
            
#Para establecer las estaciones
class Station(models.Model):
    STATE_CHOICES = [
        ('DISPONIBLE', 'Disponible'),
        ('LLENO', 'Lleno'),
        ('FUERA_DE_SERVICIO', 'Fuera de Servicio'),
    ]
    state = models.CharField(max_length=20, choices=STATE_CHOICES, default='DISPONIBLE')
    name = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return f'Estación ID: {self.pk}, Nombre: {self.name}, Estado: {self.state}'
