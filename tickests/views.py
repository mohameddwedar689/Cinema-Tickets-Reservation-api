from django.shortcuts import render
from django.http.response import JsonResponse
from .models import Guest , Movie , Reservation
from .serializers import GuestSerializer , MovieSerializer , ReservationSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status , filters 
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import generics , mixins
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


# use rest framework, serializers and models -- method (GET , POST)
@api_view(['GET' , 'POST'])
def json_data_with_rest_model(request):
    # GET method
    if request.method == 'GET':
        data = Guest.objects.all()
        serializer = GuestSerializer(data , many=True)
        return Response(serializer.data)
    # POST method
    elif request.method == 'POST':
        serializer = GuestSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=status.HTTP_201_CREATED)
        return Response(serializer.data , status=status.HTTP_400_BAD_REQUEST)
    
# use rest framework, serializers and models -- method (GET , PUT , DELETE)
@api_view(['GET' , 'PUT' , 'DELETE'])
def json_data_with_rest_model_pk(request , pk):
    try:
        guest = Guest.objects.get(pk = pk)
    except guest.DoesNotExists:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # GET
    if request.method == 'GET':
        serializer = GuestSerializer(guest)
        return Response(serializer.data , status=status.HTTP_200_OK)
    # PUT 
    if request.method == 'PUT':
        serializer = GuestSerializer(guest , data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=status.HTTP_200_OK)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
    # DELETE
    if request.method == 'DELETE':
        guest.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
# use rest framework, serializers and models -- method (GET , POST) (class based view)
class Cbv_List(APIView):
    # GET
    def get(self , request):
        guests = Guest.objects.all()
        serializer = GuestSerializer(guests , many = True)
        return Response(
            serializer.data , 
            status=status.HTTP_200_OK
        )
    # POST
    def post(self , request):
        serializer = GuestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
        
# use rest framework, serializers and models -- method (GET , PUT , DELETE) (class based view)
class Cbv_List_pk(APIView):
    # get the primary kay
    def get_object(self , pk):
        try:
            return Guest.objects.get(pk = pk)
        except Guest.DoesNotExist:
            raise Http404
    # GET
    def get(self, request , pk):
        guest = self.get_object(pk)
        serializer = GuestSerializer(guest)
        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )
    # PUT
    def put(self, request , pk):
        guest = self.get_object(pk)
        serializer = GuestSerializer(guest , data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_200_OK
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
    # DELETE
    def delete(self, request , pk):
        guest = self.get_object(pk)
        guest.delete()
        return Response(
            status=status.HTTP_204_NO_CONTENT
        )
        
        
        
        
# use rest framework, serializers and models -- method (GET , POST) (mixins)
class Mixins_list(mixins.ListModelMixin , mixins.CreateModelMixin , generics.GenericAPIView):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer
    # GET
    def get(self , request):
        return self.list(request)
    # POST
    def post(self , request):
        return self.create(request)
    
    
# use rest framework, serializers and models -- method (GET , PUT , DELETE) (mixins)
class Mixins_Pk(mixins.RetrieveModelMixin , mixins.UpdateModelMixin , mixins.DestroyModelMixin , generics.GenericAPIView):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer
    # GET
    def get(self , request , pk):
        return self.retrieve(request)
    # PUT
    def put(self , request , pk):
        return self.update(request)
    # DELETE
    def delete(self , request , pk):
        return self.destroy(request)