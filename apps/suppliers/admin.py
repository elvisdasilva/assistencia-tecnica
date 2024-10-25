from django.contrib import admin
from apps.suppliers.models import Supplier


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = (
        "company",
        "company_name",
        "fantasy_name",
        "cnpj",
        "cpf",
        "zip_code",
        "address",
        "district",
        "establishment_number",
        "complement",
        "city",
        "state",
        "primary_phone",
        "secondary_phone",
        "email",
        "created_at",
        "updated_at",
    )
