from django.http import HttpResponse, JsonResponse
from django.template.loader import render_to_string
from .models import Bike
from .forms import BikeForm
from django.shortcuts import redirect
from apps.qr_generator.models import QRCode
from django.shortcuts import render, get_object_or_404, redirect
from .models import Station

def inicio(request):
   
    return render(request, "inicio.html")

def bike_list(request):
    bikes = Bike.objects.all().order_by('-id')
    return render(request, "BikeApp/bike_list.html", {'bikes': bikes})

def save_bike_form(request, form, template_name):
    data = {}
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            bikes = Bike.objects.all().order_by('-id')
            data['html_bike_list'] = render_to_string('BikeApp/bike_list.html', {
                'bikes': bikes
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

def bike_create(request):
    if request.method == 'POST':
        form = BikeForm(request.POST)
    else:
        form = BikeForm()
    return save_bike_form(request, form, 'BikeApp/bike_create.html')

def bike_update(request, pk):
    bike = get_object_or_404(Bike, pk=pk)
    if request.method == 'POST':
        form = BikeForm(request.POST, instance=bike)
    else:
        form = BikeForm(instance=bike)
    return save_bike_form(request, form, 'BikeApp/bike_update.html')

def bike_delete(request, pk):
    bike = get_object_or_404(Bike, pk=pk)
    data = {}
    if request.method == 'POST':
        bike.delete()
        data['form_is_valid'] = True
        bikes = Bike.objects.all().order_by('-id')
        data['html_bike_list'] = render_to_string('BikeApp/bike_list.html', {
            'bikes': bikes
        })
    else:
        context = {'bike': bike}
        data['html_form'] = render_to_string('BikeApp/bike_delete.html', context, request=request)
    return JsonResponse(data)

def bike_create(request):
    if request.method == 'POST':
        form = BikeForm(request.POST)
        if form.is_valid():
            bike = form.save()
            bike.save()
            return redirect('bike_list')
        else:
            html = render_to_string('bike_form.html', {'form': form}, request=request)
            return JsonResponse({'success': False, 'html': html})
    else:
        form = BikeForm()
        return render(request, 'BikeApp/bike_form.html', {'form': form})
    
def bike_update(request, pk):
    bike = get_object_or_404(Bike, pk=pk)
    if request.method == 'POST':
        form = BikeForm(request.POST, instance=bike)
        if form.is_valid():
            bike = form.save()
            bike.save()
            return redirect('bike_list')
        else:
            html = render_to_string('BikeApp/bike_form.html', {'form': form}, request=request)
            return JsonResponse({'success': False, 'html': html})
    else:
        form = BikeForm(instance=bike)
        return render(request, 'BikeApp/bike_form.html', {'form': form})
    
def bike_delete(request, pk):
    bike = get_object_or_404(Bike, pk=pk)
    if request.method == 'POST':
        bike.delete()
        return redirect('bike_list')
    return render(request, 'BikeApp/bike_delete.html', {'bike': bike})

#Para manejar las estaciones

from .forms import StationForm

def station_list(request):
    stations = Station.objects.all()
    return render(request, 'BikeApp/station_list.html', {'stations': stations})

def station_detail(request, pk):
    station = get_object_or_404(Station, pk=pk)
    return render(request, 'BikeApp/station_detail.html', {'station': station})

def station_create(request):
    if request.method == "POST":
        form = StationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('station_list')
    else:
        form = StationForm()
    return render(request, 'BikeApp/station_form.html', {'form': form})

def station_update(request, pk):
    station = get_object_or_404(Station, pk=pk)
    if request.method == "POST":
        form = StationForm(request.POST, instance=station)
        if form.is_valid():
            form.save()
            return redirect('station_list')
    else:
        form = StationForm(instance=station)
    return render(request, 'BikeApp/station_form.html', {'form': form})

def station_delete(request, pk):
    station = get_object_or_404(Station, pk=pk)
    if request.method == "POST":
        station.delete()
        return redirect('station_list')
    return render(request, 'BikeApp/station_confirm_delete.html', {'station': station})



