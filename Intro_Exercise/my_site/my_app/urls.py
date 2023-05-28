from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index") # shwos up at /my_apps --PROJECT LVL urls.py
]