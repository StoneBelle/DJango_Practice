# Connect app lvl urls to project lvl urls
from django.urls import path
from . import views # "." refers to checking the folder you are currently in


# Create list called urlpatterns and add your paths
# Leave 1st param as empty str as you will define it in project lvl urls
# Having the above step automatically places the app name into the empty str once connected to project lvl urls

urlpatterns = [
   # Dynamically define the path views using <>
   # str: is a PATH CONVERTER to ensure the topic being passed in is a str
    path('<int:num_page>', views.num_page_view), # path for num_page_view, view
    path('<str:topic>/', views.news_view, name='topic-page'), # name allows you to refer to the particular path as the given name
    path('<int:num1>/<int:num2>', views.add_view),
    ]



