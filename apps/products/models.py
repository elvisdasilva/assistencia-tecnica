from django.db import models
from apps.companies.models import Company
from apps.brands.models import Brand
from apps.categories.models import Category
from apps.models.models import Model


class Product(models.Model):
    company = models.ForeignKey(Company, verbose_name="Company", related_name="Products", on_delete=models.PROTECT)
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    brand = models.ForeignKey(Brand, verbose_name="Brand", related_name="Products", on_delete=models.PROTECT)
    model = models.ForeignKey(Model, verbose_name="Model", related_name="Products", on_delete=models.PROTECT)
    category = models.ForeignKey(Category, verbose_name="Category", related_name="Products", on_delete=models.PROTECT)
    serie_number = models.CharField(max_length=255, null=True, blank=True)
    cost_price = models.DecimalField(max_digits=10, decimal_places=2)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
        ordering = ["name"]

    def __str__(self):
        return self.name
