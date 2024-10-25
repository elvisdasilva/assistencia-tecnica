from django.contrib import admin
from apps.companies.models import Company

class CompanyAdmin(admin.ModelAdmin):
    list_display = ("logo", "system_logo", "name", "cnpj", "district", "address", "establishment_number", "city", "state", "primary_phone", "secondary_phone", "email")

admin.site.register(Company, CompanyAdmin)
