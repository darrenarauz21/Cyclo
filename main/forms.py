from django import forms
from .models import Bike, Station

class BikeForm(forms.ModelForm):
    class Meta:
        model = Bike
        fields = ['state']

class StationForm(forms.ModelForm):
    class Meta:
        model = Station
        fields = ['name', 'latitude', 'longitude']
     
      