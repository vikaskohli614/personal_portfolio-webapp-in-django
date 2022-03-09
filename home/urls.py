from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("",views.index, name='home'),
    path("index",views.index, name='home'),
    path("services",views.services, name='services'),
    path("MyCV",views.Mycv, name='MyCV'),
    path("Blog",views.blog, name='Blog'),
    path("contact",views.contact, name='contact')
]