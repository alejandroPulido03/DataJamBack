from django.urls import path
from .services.survey_question_service import SurveyQuestionView
from .services.survey_response_service import SurveyResponseView
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path("survey_questions/", SurveyQuestionView.as_view()),
    path("survey_questions/<int:pk>/", SurveyQuestionView.as_view()),
    path("survey_responses/", SurveyResponseView.as_view()),
    path("survey_responses/<int:pk>/", SurveyResponseView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
