from django.http import HttpResponse
from django.shortcuts import render

from homes.models import ApartmentRent, ApartmentSale, Room

MADRID_COORDS = (40.416775, -3.703790)
MADRID_ADDRESS = 'Madrid, Spain'


def index(request):
    apartment_sales = ApartmentSale.objects.filter(featured__gt=0).order_by('featured')
    apartment_rents = ApartmentRent.objects.filter(featured__gt=0).order_by('featured')
    rooms = Room.objects.filter(featured__gt=0).order_by('featured')
    context = {
        'apartment_sales': apartment_sales,
        'apartment_rents': apartment_rents,
        'rooms': rooms,
    }
    return render(request, "homes/index.html", context)


def rooms(request):
    map_center = request.GET.get('center', MADRID_COORDS)
    results = Room.objects.all()
    context = {'map_center': map_center, 'results': results}
    return render(request, "homes/rooms.html", context)


def rent(request):
    latitude = request.GET.get('latitude', MADRID_COORDS[1])
    longitude = request.GET.get('longitude', MADRID_COORDS[0])
    address = request.GET.get('address', MADRID_ADDRESS)
    results = ApartmentRent.objects.all()
    initial = {
        'latitude': latitude,
        'longitude': longitude,
        'address': address,
    }
    #form = FilterApartmentRentForm(initial=initial)
    context = {
        'latitude': latitude,
        'longitude': longitude,
        'address': address,
        'results': results,
        #'form': form,
    }
    return render(request, "homes/rent.html", context)


def rent_map(request):
    longitude = request.GET.get('longitude', MADRID_COORDS[0])
    latitude = request.GET.get('latitude', MADRID_COORDS[1])
    results = ApartmentRent.objects.all()
    context = {
        'latitude': latitude,
        'longitude': longitude,
        'results': results,
    }
    return render(request, "homes/rent_map.html", context)


def sale(request):
    results = ApartmentSale.objects.all()
    context = {'results': results}
    return render(request, "homes/sale.html", context)
