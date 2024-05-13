from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ..models import Employee
from ..logic.employee_email_logic import send_emails

@api_view(["GET"])
def make_anonymous_survey_link(request, company_pk):
    employee = Employee(company_id=company_pk)
    employee.save()
    return Response({
        "employee_id": employee.employee_uuid,
        "company_id": company_pk,
    }, status=status.HTTP_200_OK)

@api_view(["POST"])
def send_emails_endpoint(request, company_pk):
    send_emails(company_pk)
    return Response({"message": "Emails sent successfully"}, status=status.HTTP_200_OK)