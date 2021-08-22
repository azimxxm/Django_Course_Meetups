from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name='all-meetups'),
    path('<slug:meetup_slug>/success', views.confirn_registration, name='confirn_registration'),
    path('<slug:meetup_slug>', views.meetup_details, name='meetup-details'),
]

