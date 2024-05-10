from rest_framework import serializers
from .models import Badge, CompanyBadge
from companies.models import Company

class BadgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Badge
        fields = ['id', 'title', 'image_id', 'description']

class CompanyBadgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyBadge
        fields = ['id', 'date_obtained', 'date_expiration', 'company', 'associated_badge']
