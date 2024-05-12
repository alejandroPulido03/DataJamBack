from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from ..models import SurveyConsolidated
from ..logic import SurveyConsolidatedSerializer, updateSurveyConsolidated


@api_view(["GET"])
def get_survey_consolidated_metrics(request, pk):
    consolidated = SurveyConsolidated.objects.get(pk=pk)
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
