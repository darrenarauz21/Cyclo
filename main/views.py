from django.shortcuts import render
from .models import *



def inicio(request):
    posts = Bike.objects.all()
    posts = Bike.objects.filter().order_by('-dateTime')
    return render(request, "inicio.html", {'posts':posts})
