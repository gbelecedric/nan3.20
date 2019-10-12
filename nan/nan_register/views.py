from django.shortcuts import render
from .models import *

# Create your views here.
def register(request):
    templates_name = 'pages/register.html'
    data = {}
    return render(request,templates_name,data)