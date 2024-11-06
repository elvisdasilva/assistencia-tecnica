from django.db import models
from apps.companies.models import Company
from apps.suppliers.models import Supplier


class Service(models.Model):
    company = models.ForeignKey(Company, verbose_name="Company", on_delete=models.PROTECT)
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    supplier = models.ForeignKey(Supplier, verbose_name="Supplier", null=True, blank=True, on_delete=models.PROTECT)
    cost_price = models.DecimalField(max_digits=10, decimal_places=2)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"
        ordering = ["name"]

    def __str__(self):
        return self.name
