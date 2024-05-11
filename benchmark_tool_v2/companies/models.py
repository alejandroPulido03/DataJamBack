from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.
class Industry(models.Model):
    name = models.CharField(max_length=100)


class Company(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    image_profile_id = models.CharField(max_length=100, null=True)
    industry = models.ForeignKey(Industry, on_delete=models.CASCADE)
    number_of_employees = models.IntegerField()
    score = models.FloatField(null=True)
    isVisible = models.BooleanField()
    isAnonymized = models.BooleanField()


class EmployeeEmail(models.Model):
    email = models.EmailField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    area = models.CharField(max_length=100)
    last_email_sent = models.DateTimeField(null=True)


class Employee(models.Model):
    employee_uuid = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    area = models.CharField(max_length=100, null=True)
