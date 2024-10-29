from django.contrib import admin
from django.contrib.auth.models import User
from .views import SendResetPasswordEmailView


class UserAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        if not change:
            obj.set_unusable_password()
            obj.save()
            SendResetPasswordEmailView().send_email(obj)


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
