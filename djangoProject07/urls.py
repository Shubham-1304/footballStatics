"""djangoProject07 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
import http
from django.contrib import admin
from django.urls import path,include
from django.http import HttpResponse

paths={'<h1>For Players having score above 90: api/</h1> <h1>For overall score grouped by nationality:api/overall</h1>'}

def home(request):
    return HttpResponse(paths)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home),
    path('api/',include('api.urls')),
]
