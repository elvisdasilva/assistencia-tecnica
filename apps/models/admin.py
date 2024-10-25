from django.contrib import admin
from .models import Model


@admin.register(Model)
class ModelAdmin(admin.ModelAdmin):
    list_display = ("company", "name", "description", "created_at", "updated_at")