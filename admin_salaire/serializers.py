from rest_framework import serializers
from .models import Employe

class EmployeSerializer(serializers.ModelSerializer):
    obs = serializers.SerializerMethodField()
    
    class Meta:
        model = Employe
        fields = ["id", "nom", "salaire", "obs"]
        read_only_fields = ["id"]

    def get_obs(self, obj):
        if obj.salaire <= 1000:
            return "Mediocre"
        elif obj.salaire <= 5000:
            return "Moyen"
        else:
            return "Grand"