from django.shortcuts import render
from rest_framework import viewsets
from .models import Order
from .serilalizers import OrderSerializer
# Create your views here.

class orderinfo(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer