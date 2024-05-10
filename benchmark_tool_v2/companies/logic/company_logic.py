from rest_framework import serializers
from ..models import Company
from rest_framework.validators import UniqueValidator


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = "__all__"
        validators = [UniqueValidator(queryset=Company.objects.all())]

    def validate_number_of_employees(self, value):
        if value < 0:
            raise serializers.ValidationError("Number of employees must be positive")
        return value
