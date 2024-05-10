from django.shortcuts import render
from rest_framework import viewsets
from .models import Badge, CompanyBadge
from .serializers import BadgeSerializer, CompanyBadgeSerializer

class BadgeViewSet(viewsets.ModelViewSet):
    queryset = Badge.objects.all()
    serializer_class = BadgeSerializer

class CompanyBadgeViewSet(viewsets.ModelViewSet):
    queryset = CompanyBadge.objects.all()
    serializer_class = CompanyBadgeSerializer

