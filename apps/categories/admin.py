from django.contrib import admin
from apps.categories.models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("company", "name", "description", "created_at", "updated_at")