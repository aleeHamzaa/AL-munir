from django.http import request
from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import mixins
from rest_framework import generics
from .serializers import Productserializer,Product1serializer
from .models import Product, Product_1
class Productviewset(viewsets.ModelViewSet):
    queryset=Product.objects.all()
    serializer_class=Productserializer
class Product1viewset(viewsets.ModelViewSet):
    queryset=Product_1.objects.all()
    serializer_class=Product1serializer