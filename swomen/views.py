# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, 'swomen/index.html')


def homeview(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, 'swomen/sidebar.html')