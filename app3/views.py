from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def view5(request):
    return HttpResponse('<h1>view five is executing</h1>')
def view6(request):
    return HttpResponse('<h1>view six is executing</h1>')
