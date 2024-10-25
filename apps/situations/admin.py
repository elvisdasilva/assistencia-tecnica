from django.contrib import admin
from apps.situations.models import Situation


@admin.register(Situation)
class SituationAdmin(admin.ModelAdmin):
    list_display = ("company", "name", "description", "created_at", "updated_at")