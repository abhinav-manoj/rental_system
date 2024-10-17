from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('index/',views.index,name='index'),
    path('create/',views.create,name='create'),
    path('details/<pk>',views.details,name='details'),
    path('chat/<pk>',views.chat,name='chat'),
    path('search/', views.search, name='search'),
    
    path('',views.index,name='index')
]