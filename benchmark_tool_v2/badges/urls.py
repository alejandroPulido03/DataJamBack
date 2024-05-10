from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BadgeViewSet, CompanyBadgeViewSet

router = DefaultRouter()
router.register(r'badges', BadgeViewSet)
router.register(r'company-badges', CompanyBadgeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
