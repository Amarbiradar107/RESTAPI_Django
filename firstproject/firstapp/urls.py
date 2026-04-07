from django.contrib import admin
from django.urls import path
from .views import home,movie_detail

urlpatterns = [
    path('home/', home, name='home'),
    path('movie/<str:id>/', movie_detail, name='movie_detail'),
]