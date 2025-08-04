from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import *
# Create your views here.

def initHome(request):
    somes = some.objects.all()
    return render(request, "initial/initialHome.html", context = {'somes':somes})

def some_views(request):
    imp = get_object_or_404(some, some.id)
    return render(request, 'initial/some.html', {'imp' : imp})