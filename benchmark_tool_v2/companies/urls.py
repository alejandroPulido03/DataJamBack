from django.urls import path
from .services.company_service import CompanyView, EmployeeEmailView
from .services.industry_service import IndustryView
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path("companies/", CompanyView.as_view()),
    path("companies/<int:company_pk>/", CompanyView.as_view()),
    path("companies/<int:company_pk>/employee_emails/", EmployeeEmailView.as_view()),
    path(
        "companies/<int:company_pk>/employee_emails/<int:employee_email_pk>/",
        EmployeeEmailView.as_view(),
    ),
    path("industries/", IndustryView.as_view()),
    path("industries/<int:pk>/", IndustryView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

