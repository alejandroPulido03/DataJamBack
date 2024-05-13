from django.urls import path
from .services.survey_question_service import SurveyQuestionView
from .services.survey_response_service import (
    SurveyResponseView,
    save_all_responses,
    get_survey_responses_by_consolidated_and_question,
)
from .services.survey_consolidated_service import get_survey_consolidated_metrics
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path("survey_questions/", SurveyQuestionView.as_view()),
    path("survey_questions/<int:pk>/", SurveyQuestionView.as_view()),
    path("survey_responses/", SurveyResponseView.as_view()),
    path("survey_responses/massive/", save_all_responses),
    path("survey_responses/<int:pk>/", SurveyResponseView.as_view()),
    path(
        "survey_consolidated_metrics/<int:company_pk>/", get_survey_consolidated_metrics
    ),
    path(
        "survey_responses/<int:consolidated_id>/<int:question_id>/",
        get_survey_responses_by_consolidated_and_question,
    ),
]

urlpatterns = format_suffix_patterns(urlpatterns)
