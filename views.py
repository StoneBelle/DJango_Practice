from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseRedirect, HttpResponseNotFound, Http404
from django.urls import reverse

# Create your views here.

articles = {
    'sports': 'Sports Page',
    'finance': 'Finance Page',
    'politics': 'Politics Page'
}


def news_view(request, topic):
    # You can use try & accept to check if a client input exists or not
    try:
        result = articles[topic]
        return HttpResponse(articles[topic])
    except:
        result = "No page for that topic."
        # raise HttpResponseNotFound(result)
        raise Http404("404 Generic Error")

def num_page_view(request, num_page):
    # domain.com/my_app/0
    topics_list = list(articles.keys()) # places the article keys into a list
    topic = topics_list[num_page]

    # webpage = reverse('topic-page', args=[topic]) # args must always be passed as a list even if its 1 item
    # return HttpResponseRedirect(webpage)
    return HttpResponseRedirect(reverse('topic-page', args=[topic]))  ### IDEAL FORMAT

def add_view(request, num1, num2):
    # domain.com/my_app/3/4 --> 7
    add_result = num1 + num2
    result = f"{num1} + {num2} = {add_result}"
    return HttpResponse(str(result))



