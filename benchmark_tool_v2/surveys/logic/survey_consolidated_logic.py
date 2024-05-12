from rest_framework import serializers
from ..models import SurveyConsolidated, SurveyResponse
from django.db.models import Avg

class SurveyConsolidatedSerializer(serializers.ModelSerializer):
    class Meta:
        model = SurveyConsolidated
        fields = '__all__'


def updateSurveyConsolidated(consolidated):
    responses = SurveyResponse.objects.filter(survey_consolidated=consolidated)
    new_score = responses.aaggregate(score=Avg('score'))['score']
    consolidated.score = new_score
    consolidated.save()
    num_responses = responses.count()
    ordered = responses.order_by('-score')
    highest_score = ordered.first().score
    lowest_score = ordered.last().score

    risk = ""
    if new_score < 3:
        risk = "Low"
    elif new_score < 6:
        risk = "Medium"
    else:
        risk = "High"

    return consolidated, num_responses, highest_score, lowest_score, risk
