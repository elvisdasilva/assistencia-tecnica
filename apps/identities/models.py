from django.db import models
from django.contrib.auth.models import AbstractUser
from apps.companies.models import Company

class Identity(AbstractUser):
    company = models.ForeignKey(Company, verbose_name="Company", on_delete=models.PROTECT, null=True, blank=True, default=None)

    class Meta:
        verbose_name = "Identity"
        verbose_name_plural = "Identities"

    def __str__(self):
        return self.company