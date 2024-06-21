from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string
from .models import Bike
from .forms import BikeForm
from django.shortcuts import redirect
from apps.qr_generator.models import QRCode

def inicio(request):
   
    return render(request, "inicio.html")

def bike(request):
    bike = Bike.objects.all().order_by('-id')
    return render(request, "bike.html", {'bike': bike})

def bike_create(request):
    if request.method == 'POST':
        form = BikeForm(request.POST)
        if form.is_valid():
            bike = form.save()
            # Generar código QR después de guardar la bicicleta
            bike.save()
            return redirect('bike') 
           # return JsonResponse({'success': True})
        else:
            html = render_to_string('bike_create.html', {'form': form}, request=request)
            return JsonResponse({'success': False, 'html': html})
    else:
        form = BikeForm()
        return render(request, 'bike_create.html', {'form': form})



