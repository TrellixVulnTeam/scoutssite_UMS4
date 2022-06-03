from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hey Tijl ge ziet er weer zo goed uit vandaag ;)")
# Create your views here.
