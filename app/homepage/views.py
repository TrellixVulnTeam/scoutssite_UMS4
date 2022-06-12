from tokenize import Pointfloat
from django.shortcuts import render
from django.http import HttpResponse
from .forms import ProjectForm


def index(request):
    form = ProjectForm()
    return render(request, "base.html", {'form': form})
# Create your views here.
