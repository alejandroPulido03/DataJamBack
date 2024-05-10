from django.db import models


# Create your models here.
class Industry(models.Model):
    name = models.CharField(max_length=100)
    image_profile_id = models.CharField(max_length=100)


class Company(models.Model):
    name = models.CharField(max_length=100)
    image_profile_id = models.CharField(max_length=100)
    industry = models.ForeignKey(Industry, on_delete=models.CASCADE)
    number_of_employees = models.IntegerField()
    score = models.FloatField()
    isVisible = models.BooleanField()
    isAnonymized = models.BooleanField()


class EmployeeEmail(models.Model):
    email = models.EmailField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    area = models.CharField(max_length=100)
    last_email_sent = models.DateTimeField()


class Employee(models.Model):
    employee_id = models.CharField(max_length=100, primary_key=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    area = models.CharField(max_length=100)
