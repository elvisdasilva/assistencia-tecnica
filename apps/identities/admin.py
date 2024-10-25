from django.contrib import admin
from apps.identities.models import Identity
from django.core.mail import send_mail
import random
import string
from core.settings import EMAIL_HOST_USER
from django.template.loader import render_to_string


@admin.register(Identity)
class IdentityAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "company")

    def save_model(self, request, obj, form, change):
        if not change:
            password = "".join(
                random.choice(string.ascii_letters + string.digits) for _ in range(10)
            )
            obj.set_password(password)

            send_mail(
                "Usuário criado com sucesso",
                render_to_string(
                    "emails/password_reset_email.txt",
                    {
                        "username": obj.username,
                        "password": password,
                    },
                ),
                EMAIL_HOST_USER,
                [obj.email],
                fail_silently=False,
            )

        super().save_model(request, obj, form, change)