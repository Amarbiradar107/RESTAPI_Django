from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

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

@api_view(['GET','PUT','DELETE'])
def movie_detail(request,id):

    if request.method == "GET":
        try:
            movie = Movie.objects.get(id=id)
        except Movie.DoesNotExist:
            return Response({'error': 'Movie not found'}, status=404)

        movieserializer = MovieSerializer(movie)
        return Response(movieserializer.data)

    if request.method == "PUT":
        try:
            movie = Movie.objects.get(id=id)
        except Movie.DoesNotExist:
            return Response({'error': 'Movie not found'}, status=404)

        movieserializer = MovieSerializer(movie, data=request.data)
        if movieserializer.is_valid():
            movieserializer.save()
            return Response(movieserializer.data)
        return Response(movieserializer.errors, status=400)

    if request.method == "DELETE":
        try:
            movie = Movie.objects.get(id=id)
        except Movie.DoesNotExist:
            return Response({'error': 'Movie not found'}, status=404)

        movie.delete()
        return Response(status=204)



    # movie = Movie.objects()
    # movieserializer = MovieSerializer(movie,many=True)
    # return Response(movieserializer.data)
