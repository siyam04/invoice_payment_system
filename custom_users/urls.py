from django.urls import path

from .views import registration


app_name = 'custom_users'


urlpatterns = [

    path('registration/', registration, name='registration'),

]


