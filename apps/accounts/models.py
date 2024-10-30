from django.contrib.auth.models import AbstractUser
from django.db import models
from apps.companies.models import Company


class User(AbstractUser):
    company = models.ForeignKey(Company, verbose_name="Company", on_delete=models.PROTECT, null=True, blank=True)