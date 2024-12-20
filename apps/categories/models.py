from django.db import models
from apps.companies.models import Company


class Category(models.Model):
    company = models.ForeignKey(Company, verbose_name="Company", on_delete=models.PROTECT) 
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ['name']

    def __str__(self):
        return self.name
