from django.contrib import admin
from apps.accounts.views import SendResetPasswordEmailView
from apps.accounts.models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "is_active", "is_staff", "is_superuser", "company")
    filter_horizontal = ("groups", "user_permissions")

    def save_model(self, request, obj, form, change):
        if not change:
            obj.set_unusable_password()
            obj.save()
            SendResetPasswordEmailView().send_email(obj)

        else:
            obj.save()


admin.site.register(User, UserAdmin)
