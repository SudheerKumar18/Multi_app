"""
URL configuration for multi project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
import app1,app2
from app3.views import *
from app4.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('app1/',include('app1.urls')),
    path('app2/',include('app2.urls')),
    path('view5/',view5,name='view5'),
    path('view6/',view6,name='view6'),
    path('view7/',view7,name='view7'),
    path('view8/',view8,name='view8'),
]
