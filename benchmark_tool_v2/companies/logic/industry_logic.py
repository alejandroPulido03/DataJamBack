from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from ..models import Industry


class IndustrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Industry
        fields = "__all__"
        validators = [
            UniqueValidator(queryset=Industry.objects.all())
        ]

