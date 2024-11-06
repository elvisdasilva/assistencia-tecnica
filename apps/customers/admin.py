from django.contrib import admin
from apps.customers.models import Customers


@admin.register(Customers)
class CustomerAdmin(admin.ModelAdmin):
    list_display = [
        "first_name",
        "last_name",
        "cpf",
        "cnpj",
        "type",
        "zip_code",
        "address",
        "district",
        "house_number",
        "complement",
        "city",
        "state",
        "primary_phone",
        "secondary_phone",
        "email",
        "created_at",
        "updated_at",
    ]

    exclude = ("company",)

    def get_queryset(self, request):
        return super().get_queryset(request).filter(company=request.user.company)

    def save_model(self, request, obj, form, change):
        company = request.user.company
        obj.company = company
        return super().save_model(request, obj, form, change)
