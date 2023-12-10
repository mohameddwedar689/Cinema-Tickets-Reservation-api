from django.urls import path
from . import views 

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

]