from django.contrib import admin
from .views import SendResetPasswordEmailView
from .models import User


class UserAdmin(admin.ModelAdmin):
    filter_horizontal = ("groups", "user_permissions")
    
    def save_model(self, request, obj, form, change):
        if not change:
            obj.set_unusable_password()
            obj.is_active = False
            obj.save()
            SendResetPasswordEmailView().send_email(obj)


admin.site.register(User, UserAdmin)
