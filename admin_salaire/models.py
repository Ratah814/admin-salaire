from django.db import models
import uuid 

class Employe(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nom = models.CharField(max_length=50)
    salaire = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return f"{self.nom} ({self.salaire})"
