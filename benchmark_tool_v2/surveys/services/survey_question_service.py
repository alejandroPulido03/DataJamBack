from rest_framework import generics
from ..models import SurveyQuestion
from ..logic.survey_question_logic import SurveyQuestionSerializer


class SurveyQuestionView(
    generics.ListCreateAPIView, 
    generics.RetrieveUpdateDestroyAPIView):
    queryset = SurveyQuestion.objects.all()
    serializer_class = SurveyQuestionSerializer
