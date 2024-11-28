from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def view7(request):
    return HttpResponse('<h1>view seven is executing</h1>')
def view8(request):
    return HttpResponse('<h1>view eight is executing</h1>')