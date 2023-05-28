from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# You can have function or class views

def index(request):
    return HttpResponse("Hello this is a view inside my_app")