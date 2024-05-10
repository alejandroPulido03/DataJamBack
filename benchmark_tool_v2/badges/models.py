from django.db import models
from companies.models import Company


# Create your models here.
class Badge(models.Model):
    title = models.CharField(max_length=100)
    image_id = models.CharField(max_length=100)
    description = models.CharField(max_length=500)


class CompanyBadge(models.Model):
    date_obtained = models.DateField()
    date_expiration = models.DateField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    asocciated_badge = models.ForeignKey(Badge, on_delete=models.CASCADE)
