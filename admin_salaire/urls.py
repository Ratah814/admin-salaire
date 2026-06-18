
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('employes/', views.EmployeListCreatView.as_view()),
    path('employes/<uuid:id>', views.EmployeUpdateDeleteView.as_view())
]
