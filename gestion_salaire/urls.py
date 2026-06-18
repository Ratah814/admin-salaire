
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin_salaire/', include('admin_salaire.urls')),
]
