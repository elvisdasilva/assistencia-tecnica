from django.db import models
from apps.companies.models import Company


class Situation(models.Model):
    company = models.ForeignKey(Company, verbose_name="Category", on_delete=models.PROTECT) 
    description = models.TextField(null=True, blank=True) 
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)