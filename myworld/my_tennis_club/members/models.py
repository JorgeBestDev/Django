from django.db import models

# Create your models here.
class Member(models.Model):
  idMiembro = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
  nombreMiembro = models.CharField(max_length=255)
  apellidoMiembro = models.CharField(max_length=255)
  telefonoMiembro = models.IntegerField(null=True)
  fechaIngreso = models.DateField(null=True)