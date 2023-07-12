from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

 
def mor_view(request):
    msg = '<h1> Good Morning </h1>'
    return HttpResponse(msg)

def aft_view(request):
    msg = '<h1> Good Afternoon </h1>'
    return HttpResponse(msg)

def eve_view(request):
    msg = '<h1> Good Evening</h1>'
    return HttpResponse(msg)

def nig_view(request):
    msg = '<h1> Good Night </h1>'
    return HttpResponse(msg)
