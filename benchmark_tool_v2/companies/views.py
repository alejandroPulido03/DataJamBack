from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def loginCompany(request):
    if request.method == "POST":
        user = request.POST['user']
        password = request.POST['password']

        #Verificar credenciales
        user = authenticate(request, user, password)
        if user is not None:
            login(request, user)
            print(user)
            return HttpResponse('Loggeado')
        else:
            return HttpResponse('Usuario invalido')
    else:
        return HttpResponse('Error!')
 