from django.shortcuts import render

# Create your views here.
from django.shortcuts import HttpResponse

def homePageView(request):
    return HttpResponse("Hello, World!")