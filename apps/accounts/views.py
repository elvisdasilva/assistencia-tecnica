from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.urls import reverse
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.views import View
from core.settings import EMAIL_HOST_USER
from django.contrib.auth.models import User


class SendResetPasswordEmailView(View):
    def send_email(self, user):
        token_generator = PasswordResetTokenGenerator()
        token = token_generator.make_token(user)
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        reset_url = reverse("password_reset_confirm", kwargs={"uidb64": uid, "token": token})

        full_reset_url = f"http://localhost:8000{reset_url}"

        subject = "Redefinição de Senha"
        html_content = render_to_string("accounts/reset_password_email.html", context={"user": user, "reset_url": full_reset_url},)
        msg = EmailMultiAlternatives(
            subject,
            html_content,
            EMAIL_HOST_USER,
            [user.email],
        )

        msg.attach_alternative(html_content, "text/html")
        msg.send()
    