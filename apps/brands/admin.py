from django.contrib import admin
from apps.brands.models import Brand


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ("company", "name", "description", "created_at", "updated_at")