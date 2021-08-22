from django.shortcuts import render, redirect
from .models import Meetup
from .forms import *
# Create your views here.


def index(request):
    meetups = Meetup.objects.all()
    return render(request, 'meetups/index.html', {'meetups':meetups})


def meetup_details(request, meetup_slug):
    try:
        if request.method == "GET":
            selected_meetup = Meetup.objects.get(slug=meetup_slug)
            resgistration_form = RegistrationForm()
        else:
            selected_meetup = Meetup.objects.get(slug=meetup_slug)
            resgistration_form = RegistrationForm(request.POST)
            if resgistration_form.is_valid():
                participant = resgistration_form.save()
                selected_meetup.participant.add(participant)
                return redirect('confirn_registration', meetup_slug=meetup_slug)
                

        return render(request, 'meetups/meetup_details.html', {
            'meetup_found':True,
            'meetup':selected_meetup,
            'form':resgistration_form,
        })
    except Exception as exc:
        return render(request,'meetups/meetup_details.html', {
            'meetup_found':False
        } )

def confirn_registration(request, meetup_slug):
    meetup = Meetup.objects.get(slug=meetup_slug)
    return render(request, 'meetups/registration-success.html', {
        'organizer_email':meetup.organizer_email
    })