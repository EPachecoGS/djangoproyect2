from django.db import models

# Create your models here.
class personas(models.Model):
    id_personas = models.AutoField(auto_created = True, primary_key=True, serialize = False)
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    def __str__(self):
        return f'{self.NombreUsuario},{self.name},{self.password}'