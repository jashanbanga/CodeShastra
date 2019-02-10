from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class RailwayAdmin(models.Model):
	railwayEmpId = models.CharField(max_length=100)
	railwayEmployee = models.OneToOneField(User, on_delete=models.CASCADE)

class CollegeAdmin(models.Model):
	collegeEmpId = models.CharField(max_length=100)
	collegeEmployee = models.OneToOneField(User, on_delete=models.CASCADE)
