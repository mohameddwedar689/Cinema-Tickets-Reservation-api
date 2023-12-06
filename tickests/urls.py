from django.urls import path
from . import views 

urlpatterns = [
    # url that route to view return static json data (no rest , no model)
    path('static_data/' , views.static_json_data),
]