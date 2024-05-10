from django.contrib import admin

import companies.models, surveys.models, badges.models

# Register your models here.
admin.site.register(
    [
        companies.models.Company,
        companies.models.Employee,
        companies.models.EmployeeEmail,
        companies.models.Industry,
        surveys.models.SurveyQuestion,
        surveys.models.SurveyResponse,
        surveys.models.SurveyConsolidated,
        badges.models.Badge,
        badges.models.CompanyBadge,
    ]
)
