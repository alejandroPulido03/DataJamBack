from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from ..models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"
        validators = [UniqueValidator(queryset=Employee.objects.all())]
