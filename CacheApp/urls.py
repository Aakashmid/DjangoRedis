
from django.contrib import admin
from django.urls import path,include
from CacheApp import  views


urlpatterns = [
    path('',views.home,name='Home')
]