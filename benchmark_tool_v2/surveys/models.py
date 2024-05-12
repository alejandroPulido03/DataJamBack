from django.db import models
from companies.models import Company, Employee

class SurveyQuestion(models.Model):
    type_questions = {
        "NUMERIC": "NUMERIC",
        "PERCENTAGE": "PERCENTAGE",
        "SELECT": "SELECT",
        "TEXT": "TEXT",
        "YES_NO": "YES_NO",
    }

    statement = models.CharField(max_length=1000)
    asociated_risk = models.CharField(max_length=100)
    type_question = models.CharField(max_length=20, choices=type_questions.items())
    question_config = models.JSONField()


class SurveyConsolidated(models.Model):
    asociated_company = models.ForeignKey(Company, on_delete=models.CASCADE)
    score = models.FloatField()
    date = models.DateField()
    expiration_date = models.DateField()


class SurveyResponse(models.Model):
    respondent = models.ForeignKey(Employee, on_delete=models.DO_NOTHING)
    survey_consolidated = models.ForeignKey(
        SurveyConsolidated, on_delete=models.CASCADE
    )
    survey_question = models.ForeignKey(SurveyQuestion, on_delete=models.DO_NOTHING)
    answer = models.CharField(max_length=100)
    comment = models.CharField(max_length=500)
    score = models.FloatField()
