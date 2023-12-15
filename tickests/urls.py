from django.urls import path , include
from . import views 
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register('guests' , views.ViewSets_guest)
router.register('movies' , views.ViewSets_movie)
router.register('reservations' , views.ViewSets_reservation)

urlpatterns = [
    # url that route to view return static json data (no rest , no model)
    path('static_data/' , views.static_json_data),
    # url for retrive json data form model in database without using rest framework
    path('model_data/' , views.json_data_from_model),
    # url for two method (GET , POST) with using rest framework, models and serializers
    path('rest/fbv_list/' , views.json_data_with_rest_model),
    # url for three method (GET , PUT , DELETE) with using rest framework, models and serializers
    path('rest/fbv_list/<int:pk>' , views.json_data_with_rest_model_pk),
    # url for two method (GET , POST) with using rest framework, models and serializers (Class Based View)
    path('rest/cbv_list/', views.Cbv_List.as_view()),
    # url for three method (GET , PUT , DELETE) with using rest framework, models and serializers (Class Based View)
    path('rest/cbv_list/<int:pk>', views.Cbv_List_pk.as_view()),
    # url for two method (GET , POST) with using rest framework, models and serializers (mixins)
    path('rest/mixins/' , views.Mixins_list.as_view()),
    # url for three method (GET , PUT , DELETE) with using rest framework, models and serializers (mixins)
    path('rest/mixins/<int:pk>' , views.Mixins_Pk.as_view()),
    # url for two method (GET , POST) with using rest framework, models and serializers (Generics)
    path('rest/generics/' , views.Generics_list.as_view()),
    # url for three method (GET , PUT , DELETE) with using rest framework, models and serializers (Generics)
    path('rest/generics/<int:pk>' , views.Generics_Pk.as_view()),
    # url for three method (GET , POST , PUT , DELETE) with using rest framework, models and serializers (Viewsets)
    path('rest/viewsets/' , include(router.urls)),
    # endpoint to find a movie (function based view)
    path('fbv/find/' , views.find_movie),
    # endpoint to make a new reservation
    path('fbv/new/', views.new_reservation),
    # rest framework auto
    path('api-auth' , include('rest_framework.urls')),
    # token
    path('api-token-auth' , obtain_auth_token)
]