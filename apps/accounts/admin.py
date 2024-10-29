from django.contrib import admin
from django.contrib.auth.models import User
from .views import send_reset_password_email


class UserAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        if not change:  # Se for um novo usuário
            obj.set_unusable_password()
            obj.save()
            send_reset_password_email(obj)


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
