from django.contrib import admin
from apps.brands.models import Brand


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ("name", "company", "description", "created_at", "updated_at")

    exclude = ("company",)

    def save_model(self, request, obj, form, change):
        obj.company = request.user.company
        super().save_model(request, obj, form, change)
