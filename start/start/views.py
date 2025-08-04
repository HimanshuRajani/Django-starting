from django.http import HttpResponse
from django.shortcuts import render
from initial.models import some

def home(request):
    somes = some.objects.all()
    return render(request, "website/home.html", {'somes':somes})

def about(request):
    return render(request, "website/about.html")

def contact(request):
    return render(request, "website/contact.html")