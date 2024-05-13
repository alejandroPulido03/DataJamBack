from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from ..logic.survey_consolidated_logic import SurveyConsolidatedSerializer, updateSurveyConsolidated, getLastCompanyConsolidated


@api_view(["GET"])
def get_survey_consolidated_metrics(request, company_pk):
    consolidated = getLastCompanyConsolidated(company_pk)
    consolidated, num_responses, highest_score, lowest_score, risk = (
        updateSurveyConsolidated(consolidated)
    )
    return Response(
        {
            "consolidated": SurveyConsolidatedSerializer(consolidated).data,
            "num_responses": num_responses,
            "highest_score": highest_score,
            "lowest_score": lowest_score,
            "risk": risk,
        },
        status=status.HTTP_200_OK,
    )