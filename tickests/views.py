from django.shortcuts import render
from django.http.response import JsonResponse
# Create your views here.

# Fisrt Type
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