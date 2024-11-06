from django.contrib import admin
from apps.services.models import Service


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "description",
        "supplier",
        "cost_price",
        "selling_price",
        "created_at",
        "updated_at",
    )

    exclude = ("company",)

    def get_queryset(self, request):
        return super().get_queryset(request).filter(company=request.user.company)

    def save_model(self, request, obj, form, change):
        company = request.user.company
        obj.company = company
        return super().save_model(request, obj, form, change)