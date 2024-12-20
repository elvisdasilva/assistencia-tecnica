from django.db import models
from apps.companies.models import Company


class Brand(models.Model):
    company = models.ForeignKey(Company, verbose_name="Company", on_delete=models.PROTECT) 
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Brand"
        verbose_name_plural = "Brands"
        ordering = ['name']

    def __str__(self):
        return self.name