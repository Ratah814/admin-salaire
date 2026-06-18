import logging
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.shortcuts import render
from rest_framework import generics
from .models import Employe
from .serializers import EmployeSerializer

logger = logging.getLogger(__name__)

@method_decorator(cache_page(60 * 5), name='get')  # Cache the GET request for 5 minutes
class EmployeListCreatView(generics.ListCreateAPIView):
    queryset = Employe.objects.all().only('id', 'nom', 'salaire')  # Optimize query to fetch only necessary fields
    serializer_class = EmployeSerializer

    def create(self, request, *args, **kwargs):
        logger.info(f"Création d'un nouvel employé : {request.data.get('nom')}")
        try:
            response = super().create(request, *args, **kwargs)
            logger.info(f"Employé créé avec succès !!")
            return response
        except Exception as e:
            logger.error(f"Erreur lors de la création de l'employé !! {e}")
            raise

class EmployeUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employe.objects.all().only('id', 'nom', 'salaire')  # Optimize query to fetch only necessary fields  
    serializer_class = EmployeSerializer
    lookup_field = 'id'