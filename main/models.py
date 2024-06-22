from django.db import models
from apps.qr_generator.models import QRCode

class Bike(models.Model):
    STATE_CHOICES = [
        ('DISPONIBLE', 'Disponible'),
        ('OCUPADO', 'Ocupado'),
        ('FUERA_DE_SERVICIO', 'Fuera de Servicio'),
    ]
    state = models.CharField(max_length=20, choices=STATE_CHOICES, default='DISPONIBLE')
    qr_code = models.OneToOneField(QRCode, on_delete=models.CASCADE, blank=True, null=True)
    
    def __str__(self):
        return f'Bicicleta ID: {self.pk}, Estado: {self.state}'
    
    def save(self, *args, **kwargs):
        if not self.pk:
            super().save(*args, **kwargs)  # Primero guarda la instancia para obtener un ID válido
            qr_code = QRCode(content=str(self.pk))
            qr_code.save()
            self.qr_code = qr_code
            super().save(*args, **kwargs)  # Guarda nuevamente para asociar el QRCode a la instancia
        else:
            super().save(*args, **kwargs)
            
#Para establecer las estaciones
class Station(models.Model):
    name = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.name

