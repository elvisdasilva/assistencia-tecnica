from django.contrib import admin
from apps.payments.models import Payment


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ("company", "name", "description", "created_at", "updated_at")