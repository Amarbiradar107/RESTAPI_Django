from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Todo,User
from .serializers import TodoSerializer,UserSerializer
from rest_framework.decorators import api_view

# Create your views here.

@api_view(['GET', 'POST'])
def todo_list(request):
    if request.method == 'GET':
        todos = Todo.objects()
        todo_serializer = TodoSerializer(todos, many=True)
        return Response(todo_serializer.data)

    if request.method == 'POST':
        todo_serializer = TodoSerializer(data=request.data)
        if todo_serializer.is_valid():
            todo_serializer.save()
            return Response(todo_serializer.data, status=201)
        return Response(todo_serializer.errors, status=400)

@api_view(['GET', 'PUT', 'DELETE'])
def todo_detail(request, id):
    if request.method == 'GET':
        try:
            todo = Todo.objects.get(id=id)
        except Todo.DoesNotExist:
            return Response(status=404)

        todo_serializer = TodoSerializer(todo)
        return Response(todo_serializer.data)

    if request.method == 'PUT':
        try:
            todo = Todo.objects.get(id=id)
        except Todo.DoesNotExist:
            return Response(status=404)

        todo_serializer = TodoSerializer(todo, data=request.data)
        if todo_serializer.is_valid():
            todo_serializer.save()
            return Response(todo_serializer.data)
        return Response(todo_serializer.errors, status=400)

    if request.method == 'DELETE':
        try:
            todo = Todo.objects.get(id=id)
        except Todo.DoesNotExist:
            return Response(status=404)
        todo.delete()
        return Response(status=204)




class user_detail(APIView):
    def get(self, request):
        user_details = User.objects()
        user_serializer = UserSerializer(user_details, many=True)
        return Response(user_serializer.data)

    def post(self,request):
        user_serializer = UserSerializer(data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data, status=201)
        return Response(user_serializer.errors, status=400)




