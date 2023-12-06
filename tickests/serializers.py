from rest_framework import serializers
from .models import Movie , Guest , Reservation

class MovieSerializer(serializers.MovieSerializer):
    class Meta:
        model = Movie
        fields = '__all__'
        
class ReservationSerializer(serializers.ReservationSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'
        
class GuestSerializer(serializers.GuestSerializer):
    class Meta:
        model = Guest
        fields = ['pk' , 'reservation' , 'name' , 'mobile']