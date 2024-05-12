from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response

from . import models
# comment: ""
# ​
# consolidated: "1"
# ​
# questionId: "1"
# ​
# respondent: "1"
# ​
# score: 0.15

@csrf_exempt
@api_view(["POST"])
def registerResponse(request):
    if request.method == "POST":
        respondent = request.data["respondent"]
        score = request.data["score"]
        question_id = request.data["questionId"]
        consolidated = request.data["consolidated"]
        comment = request.data["comment"]
        models.SurveyResponse(respondent, consolidated, question_id, "respuesta", comment, score)
        return Response({"status":'Respuesta registrada'})

    else: 
        return Response({"status":'Respuesta registrada'})
        
        