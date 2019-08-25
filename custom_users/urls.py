from django.urls import path

from .views import (

    registration,
    profile_create,
    profile_details,
    profile_edit,
)


app_name = 'custom_users'


urlpatterns = [

    path('registration/', registration, name='registration'),

    path('profile_create/', profile_create, name='profile_create'),

    path('profile_details/<int:id>/', profile_details, name='profile_details'),

    path('profile_edit/', profile_edit, name='profile_edit'),

]


