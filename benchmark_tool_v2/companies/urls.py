from django.urls import path
from . import views
from .services.company_service import CompanyView, EmployeeEmailView
from .services.industry_service import IndustryView
from .services.employee_service import make_anonymous_survey_link, send_emails_endpoint
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path("companies/login",views.loginCompany, name="loginCompany"),
    path("companies/", CompanyView.as_view()),
    path("companies/<int:company_pk>/", CompanyView.as_view()),
    path("companies/<int:company_pk>/employee_emails/", EmployeeEmailView.as_view()),
    path(
        "companies/<int:company_pk>/employee_emails/<int:employee_email_pk>/",
        EmployeeEmailView.as_view(),
    ),
    path("companies/<int:company_pk>/send_emails/", send_emails_endpoint),
    path("industries/", IndustryView.as_view()),
    path("industries/<int:pk>/", IndustryView.as_view()),

    path("make_anonymous_survey/<int:company_pk>/", make_anonymous_survey_link),
]

urlpatterns = format_suffix_patterns(urlpatterns)

