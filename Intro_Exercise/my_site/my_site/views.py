# Project lvl views file

from django.http.response import HttpResponse

def home_view(request):
    return HttpResponse('Home View')