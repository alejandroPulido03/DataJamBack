from rest_framework import generics
from ..models import SurveyResponse
from ..logic.survey_response_logic import SurveyResponseSerializer


class SurveyResponseView(generics.CreateAPIView, generics.RetrieveUpdateDestroyAPIView):
    queryset = SurveyResponse.objects.all()
    serializer_class = SurveyResponseSerializer
