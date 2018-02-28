from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from tethys_sdk.gizmos import Button

@login_required()
def home(request):
    """
    Controller for the app home page.
    """

    context = {

    }

    return render(request, 'jordimapapp/home.html', context)

def map_view(request):
    context = {

    }

    return render(request, 'jordimapapp/map_view.html', context)

def data_services(request):
    context = {

    }

    return render(request, 'jordimapapp/data_services.html', context)

def about(request):
    context = {

    }

    return render(request, 'jordimapapp/about.html', context)

def proposal(request):
    context = {

    }

    return render(request, 'jordimapapp/proposal.html', context)

def wireframes(request):
    context = {

    }

    return render(request, 'jordimapapp/wireframes.html', context)