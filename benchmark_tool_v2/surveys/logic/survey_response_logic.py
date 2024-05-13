from rest_framework import serializers, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..models import SurveyResponse
from .survey_question_logic import calculate_score, SurveyQuestionSerializer


class SurveyResponseSerializer(serializers.ModelSerializer):
    score = serializers.FloatField(read_only=True)

    class Meta:
        model = SurveyResponse
        fields = "__all__"

    def save(self, **kwargs):
        question = SurveyQuestionSerializer(self.validated_data["survey_question"])
        answer = self.validated_data["answer"]
        self.validated_data["score"] = calculate_score(question.data, answer)
        return super().save(**kwargs)
