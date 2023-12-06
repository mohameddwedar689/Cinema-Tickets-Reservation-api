from django.shortcuts import render
from django.http.response import JsonResponse
from .models import Guest , Movie , Reservation 
# Create your views here.


# no rest, no model (static date) to (Json format)
def static_json_data(request):
    guest = [
        {
            "id":1,
            "name":"mohamed",
            "age":23
        },
        {
            "id":2,
            "name":"ahmed",
            "age":23
        }
    ]
    return JsonResponse(guest , safe=False)

# no rest, from model (data form model in database without using rest framework)
def json_data_from_model(request):
    # data from guest model
    guest_data = Guest.objects.all()
    response_guest = {
        'guest': list(guest_data.values('name' , 'mobile')),
    }
    # data from movie model
    movie_data = Movie.objects.all()
    response_movie = {
        'movie': list(movie_data.values()),
    }
    # data from reservation model
    reservation_data = Reservation.objects.all()
    response_reservation = {
        'reservation': list(reservation_data.values()),
    }
    
    return JsonResponse(response_guest)