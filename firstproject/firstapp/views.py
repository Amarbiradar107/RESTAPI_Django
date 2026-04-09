from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
from rest_framework.views import APIView

from .models import Movie
from .serializers import MovieSerializer
# Create your views here.

@api_view(['GET','POST'])
def home(request):
    if request.method == 'GET':
        movie = Movie.objects()
        movieserializer = MovieSerializer(movie, many=True)
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
            return Response(movieserializer.data,status=200)
        return Response(movieserializer.errors, status=400)

    if request.method == "DELETE":
        try:
            movie = Movie.objects.get(id=id)
        except Movie.DoesNotExist:
            return Response({'error': 'Movie not found'}, status=404)

        movie.delete()
        return Response(status=204)

@api_view(['POST'])
def import_movies(request):
    """
    Fetch JSON array from external API and save to DB.
    Request body (optional): {"url": "https://example.com/api/movies/"}
    """
    url = request.data.get('https://fakestoreapi.com/products')  # change default to real endpoint
    try:
        resp = requests.get(url, timeout=10)
        resp.raise_for_status()
        payload = resp.json()
    except requests.RequestException as e:
        return Response({'error': 'Failed to fetch external API', 'details': str(e)}, status=502)
    if not isinstance(payload, list):
        return Response({'error': 'Expected a list/array from external API'}, status=400)

    created = []
    errors = []
    for item in payload:
        serializer = MovieSerializer(data=item)
        if serializer.is_valid():
            serializer.save()
            created.append(serializer.data)
        else:
            errors.append({'item': item, 'errors': serializer.errors})

    return Response({'created_count': len(created), 'created': created, 'errors': errors})



    # movie = Movie.objects()
    # movieserializer = MovieSerializer(movie,many=True)
    # return Response(movieserializer.data)
