from rest_framework import serializers
from ..models import Company

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = "__all__"
    
    def validate_name(self, value):
        if value == Company.objects.filter(name=value).first():
            raise serializers.ValidationError("Company name already exists")
        return value
    
    def validate_number_of_employees(self, value):
        if value < 0:
            raise serializers.ValidationError("Number of employees must be positive")
        return value
