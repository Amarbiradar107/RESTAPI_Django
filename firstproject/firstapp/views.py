from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Movie
from .serializers import MovieSerializer
# Create your views here.

@api_view(['GET','POST'])
def home(request):
    if request.method == 'GET':
        movie = Movie.objects()
        movieserializer = MovieSerializer(movie, many=True)
        print(movieserializer.data)
        return Response(movieserializer.data)

    if request.method == 'POST':

        movieserializer = MovieSerializer(data=request.data)
        if movieserializer.is_valid():
            movieserializer.save()
            return Response(movieserializer.data, status=201)
        return Response(movieserializer.errors, status=400)


    # movie = Movie.objects()
    # movieserializer = MovieSerializer(movie,many=True)
    # return Response(movieserializer.data)
