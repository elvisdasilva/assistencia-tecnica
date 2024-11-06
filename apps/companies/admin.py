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

    def get_queryset(self, request):
        if request.user.is_superuser:
            return super().get_queryset(request)

        return super().get_queryset(request).filter(user=request.user)
