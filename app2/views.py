from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def view3(request):
    return HttpResponse('<h1>view two is executing</h1>')
def view4(request):
    return HttpResponse('<h1>view four is executing</h1>')
