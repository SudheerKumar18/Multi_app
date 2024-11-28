from app1.views import *
from django.urls import path

urlpatterns=[
    path('view1/',view1,name='view1'),
    path('view2/',view2,name='view2'),
]