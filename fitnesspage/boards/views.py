from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("This is the landing page for Foundation Fitness.")

def forum(request):
    return HttpResponse("This is the page for Foundation Fitness's discussion forum.")

def about(request):
    return HttpResponse("This is the page for Foundation Fitness's general information.")

def contact(request):
    return HttpResponse("This is the page for Foundation Fitness's contact information.")