from app2.views import *
from django.urls import path

urlpatterns=[
    path('view3/',view3,name='view3'),
    path('view4/',view4,name='view4'),
]