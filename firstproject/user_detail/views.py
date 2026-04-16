from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import user
from .serializers import userserializer

# Create your views here.

class userlist(APIView):
    def get(self,request):
        user_details = user.objects()
        user_serailaizer = userserializer(user_details, many=True)
        return Response(user_serailaizer.data)

    def post(self,request):
        user_serailaizer = userserializer(data=request.data)
        if user_serailaizer.is_valid():
            user_serailaizer.save()
            return Response(user_serailaizer.data, status=201)
        return Response(user_serailaizer.errors, status=400)