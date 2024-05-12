from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response

# @csrf_exempt
@api_view(["POST"])
def loginCompany(request):
    if request.method == "POST":
        user = request.data["user"]
        password = request.data["password"]

        #Verificar credenciales
        user = authenticate(username=user, password=password)
        if user is not None:
            login(request, user)
            return Response({"status":'Loggeado'})
        else:
            return Response({"status":'Usuario invalido'})
