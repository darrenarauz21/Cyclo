from django.http import HttpResponse, JsonResponse
from django.template.loader import render_to_string
from .models import Bike,Station
from .forms import BikeForm
from django.shortcuts import render, get_object_or_404, redirect


def inicio(request):
   
    return render(request, "inicio.html")

def bike_list(request):
    bikes = Bike.objects.all()
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
        if form.is_valid():
            bike = form.save()
            return redirect('bike_list')
    else:
        form = BikeForm()
    return render(request, 'BikeApp/bike_create.html', {'form': form})

def bike_update(request, pk):
    bike = get_object_or_404(Bike, pk=pk)
    if request.method == 'POST':
        form = BikeForm(request.POST, instance=bike)
        if form.is_valid():
            form.save()
            return JsonResponse({'form_is_valid': True})
        else:
            return JsonResponse({'form_is_valid': False, 'html_form': render_to_string('BikeApp/bike_update.html', {'form': form, 'bike': bike}, request=request)})
    else:
        form = BikeForm(instance=bike)
    html_form = render_to_string('BikeApp/bike_update.html', {'form': form, 'bike': bike}, request=request)
    return JsonResponse({'html_form': html_form})

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
        return JsonResponse(data)
    else:
        context = {'bike': bike}
        return render(request, 'BikeApp/bike_delete.html', context)


#Para manejar las estaciones

from .forms import StationForm

def station_list(request):
    stations = Station.objects.all()
    return render(request, 'BikeApp/station_list.html', {'stations': stations})

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
    if request.method == 'POST':
        form = StationForm(request.POST, instance=station)
        if form.is_valid():
            form.save()
            return JsonResponse({'form_is_valid': True})
        else:
            return JsonResponse({'form_is_valid': False, 'html_form': render_to_string('BikeApp/station_update.html', {'form': form, 'station': station}, request=request)})
    else:
        form = StationForm(instance=station)
    html_form = render_to_string('BikeApp/station_update.html', {'form': form, 'station': station}, request=request)
    return JsonResponse({'html_form': html_form})

def station_delete(request, pk):
    station = get_object_or_404(Station, pk=pk)
    data = {}
    if request.method == 'POST':
        station.delete()
        data['form_is_valid'] = True
        station = Station.objects.all().order_by('-id')
        data['html_station_list'] = render_to_string('BikeApp/station_list.html', {
            'station': station
        })
        return JsonResponse(data)
    else:
        context = {'station': station}
        return render(request, 'BikeApp/station_delete.html', context)




