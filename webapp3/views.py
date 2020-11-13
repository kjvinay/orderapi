from django.shortcuts import render
from rest_framework import viewsets

from .serializers import companySerializer,productSerializer, orderSerializer
from .models import company,product,order


class companyView(viewsets.ModelViewSet):
    queryset = company.objects.all()
    serializer_class = companySerializer

class productView(viewsets.ModelViewSet):
    queryset = product.objects.all()
    serializer_class = productSerializer

class orderView(viewsets.ModelViewSet):
    queryset = order.objects.all()
    serializer_class = orderSerializer


