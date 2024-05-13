from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from ..models import SurveyResponse
from ..logic.survey_response_logic import SurveyResponseSerializer


class SurveyResponseView(generics.CreateAPIView, generics.RetrieveUpdateDestroyAPIView):
    queryset = SurveyResponse.objects.all()
    serializer_class = SurveyResponseSerializer


@api_view(["POST"])
def save_all_responses(request):
    responses = request.data
    response_data = []
    for response in responses:
        serializer = SurveyResponseSerializer(data=response)
        if serializer.is_valid():
            serializer.save()
            response_data.append(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    return Response(response_data, status=status.HTTP_201_CREATED)

@api_view(["GET"])
def get_survey_responses_by_consolidated_and_question(request, consolidated_id, question_id):
    responses = SurveyResponse.objects.filter(
        survey_consolidated_id=consolidated_id, survey_question_id=question_id
    )
    serializer = SurveyResponseSerializer(responses, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)