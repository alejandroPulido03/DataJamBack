from django.db import models
from companies.models import Company


# Create your models here.
class SurveyQuestion(models.Model):
    type_questions = {
        "NUMERIC": "NUMERIC",
        "PERCENTAGE": "PERCENTAGE",
        "SELECT": "SELECT",
        "TEXT": "TEXT",
    }

    statement = models.CharField(max_length=100)
    asociated_risk = models.CharField(max_length=100)
    type_question = models.CharField(max_length=20, choices=type_questions.items())
    type_chart = models.CharField(max_length=50)


class SurveyConsolidated(models.Model):
    asociated_company = models.ForeignKey(Company, on_delete=models.CASCADE)
    score = models.FloatField()
    date = models.DateField()
    expiration_date = models.DateField()


class SurveyResponse(models.Model):
    survey_consolidated = models.ForeignKey(
        SurveyConsolidated, on_delete=models.CASCADE
    )
    survey_question = models.ForeignKey(SurveyQuestion, on_delete=models.CASCADE)
    answer = models.CharField(max_length=100)
    comment = models.CharField(max_length=500)
    score = models.FloatField()
