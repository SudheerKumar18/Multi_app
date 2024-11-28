from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def view1(request):
    return HttpResponse('<h1>view one is executing</h1>')
def view2(request):
    return HttpResponse('<h1>view two is executing</h1>')

