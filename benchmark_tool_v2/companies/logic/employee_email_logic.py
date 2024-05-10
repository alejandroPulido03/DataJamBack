from rest_framework import serializers
from ..models import EmployeeEmail


class EmployeeEmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeEmail
        fields = "__all__"

    def validate_email(self, value):
        if value == EmployeeEmail.objects.filter(email=value).first():
            raise serializers.ValidationError("Email already exists")
        return value

    def validate_area(self, value):
        if value == "":
            raise serializers.ValidationError("Area must not be empty")
        return value




# TODO send emails
