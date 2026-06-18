from django.shortcuts import render
from rest_framework import generics
from .models import Employe
from .serializers import EmployeSerializer

class EmployeListCreatView(generics.ListCreateAPIView):
    queryset = Employe.objects.all()
    serializer_class = EmployeSerializer

class EmployeUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employe.objects.all()
    serializer_class = EmployeSerializer
    lookup_field = 'id'