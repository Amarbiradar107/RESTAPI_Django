from django.shortcuts import render
from rest_framework import viewsets
from .models import User
from .serializers import UserSerializer
# Create your views here.

class userinfo(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        print(request.data)  # 👈 see what is coming
        return super().create(request, *args, **kwargs)

