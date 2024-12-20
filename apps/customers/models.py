from django.db import models
from apps.companies.models import Company


class Customers(models.Model):
    STATE_CHOICES = [
        ("AC", "Acre"),
        ("AL", "Alagoas"),
        ("AP", "Amapá"),
        ("AM", "Amazonas"),
        ("BA", "Bahia"),
        ("CE", "Ceará"),
        ("DF", "Distrito Federal"),
        ("ES", "Espírito Santo"),
        ("GO", "Goiás"),
        ("MA", "Maranhão"),
        ("MT", "Mato Grosso"),
        ("MS", "Mato Grosso do Sul"),
        ("MG", "Minas Gerais"),
        ("PA", "Pará"),
        ("PB", "Paraíba"),
        ("PR", "Paraná"),
        ("PE", "Pernambuco"),
        ("PI", "Piauí"),
        ("RJ", "Rio de Janeiro"),
        ("RN", "Rio Grande do Norte"),
        ("RS", "Rio Grande do Sul"),
        ("RO", "Rondônia"),
        ("RR", "Roraima"),
        ("SC", "Santa Catarina"),
        ("SP", "São Paulo"),
        ("SE", "Sergipe"),
        ("TO", "Tocantins"),
    ]

    CUSTOMER_TYPE_CHOICES = [
        ("Physical Person", "Physical Person"),
        ("Legal Person", "Legal Person"),
    ]

    company = models.ForeignKey(Company, verbose_name="Company", on_delete=models.PROTECT)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    cnpj = models.CharField(max_length=14, null=True, blank=True, unique=True)
    cpf = models.CharField(max_length=11, null=True, blank=True, unique=True)
    type = models.CharField(choices=CUSTOMER_TYPE_CHOICES, max_length=20)
    zip_code = models.CharField(max_length=8)
    address = models.CharField(max_length=200)
    district = models.CharField(max_length=200)
    house_number = models.CharField(max_length=50)
    complement = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(choices=STATE_CHOICES, max_length=2)
    primary_phone = models.CharField(max_length=14)
    secondary_phone = models.CharField(max_length=14, null=True, blank=True)
    email = models.CharField(max_length=200, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Customer"
        verbose_name_plural = "Customers"
        ordering = ["first_name"]

    def __str__(self):
        return self.first_name
