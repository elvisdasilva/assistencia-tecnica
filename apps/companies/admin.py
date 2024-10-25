from django.contrib import admin
from apps.companies.models import Company


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = (
        "logo",
        "system_logo",
        "name",
        "cnpj",
        "district",
        "address",
        "establishment_number",
        "city",
        "state",
        "primary_phone",
        "secondary_phone",
        "email",
        "created_at",
        "updated_at",
    )