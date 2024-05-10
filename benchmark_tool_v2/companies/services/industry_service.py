from rest_framework import generics
from ..models import Industry
from ..logic.industry_logic import IndustrySerializer


class IndustryView(generics.ListCreateAPIView, generics.RetrieveAPIView):
    queryset = Industry.objects.all()
    serializer_class = IndustrySerializer
