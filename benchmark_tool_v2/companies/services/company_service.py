from ..models import Company, EmployeeEmail
from ..logic.company_logic import CompanySerializer
from ..logic.employee_email_logic import EmployeeEmailSerializer
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class CompanyView(generics.CreateAPIView, generics.RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class EmployeeEmailView(APIView):
    def post(self, request, company_pk):
        for email in request.data["emails"]:
            email["company"] = company_pk
            serializer = EmployeeEmailSerializer(data=email)
            if serializer.is_valid():
                serializer.save()
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"message": "Emails created successfully"}, status=status.HTTP_201_CREATED)

    def put(self, request, company_pk, employee_email_pk):
        employee_email = EmployeeEmail.objects.get(
            pk=employee_email_pk, company=company_pk
        )
        serializer = EmployeeEmailSerializer(employee_email, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, company_pk):
        employee_emails = EmployeeEmail.objects.filter(company=company_pk)
        serializer = EmployeeEmailSerializer(employee_emails, many=True)
        return Response(serializer.data)
