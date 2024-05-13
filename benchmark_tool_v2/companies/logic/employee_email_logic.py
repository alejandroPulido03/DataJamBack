from rest_framework import serializers
from ..models import EmployeeEmail
from rest_framework.validators import UniqueValidator
from ...benchmark_tool_v2.settings import EMAIL_HOST_USER
from django.core.mail import send_mail


class EmployeeEmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeEmail
        fields = "__all__"
        validators = [
            UniqueValidator(queryset=EmployeeEmail.objects.all())
        ]


def send_emails(company_pk):
    employees = EmployeeEmail.objects.filter(company_id=company_pk)
    for employee in employees:
        subject = 'Walk Free Survey'
        message = '''
        Hello, you have been invited to take a survey in order to measure your company\'s performance in terms of human rights and fight against modern
        slavery. Please click on the following link to start the anonymous survey: http://localhost:4200/make_anonymous_survey/''' + str(company_pk) + '''/
        '''
        receiver = employee.email
        send_mail(subject, message, EMAIL_HOST_USER, [receiver])

    
