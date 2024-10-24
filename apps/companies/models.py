from django.db import models

class Company(models.Model):
    STATE_CHOICES = [
        ('AC', 'Acre'),
        ('AL', 'Alagoas'),
        ('AP', 'Amapá'),
        ('AM', 'Amazonas'),
        ('BA', 'Bahia'),
        ('CE', 'Ceará'),
        ('DF', 'Distrito Federal'),
        ('ES', 'Espírito Santo'),
        ('GO', 'Goiás'),
        ('MA', 'Maranhão'),
        ('MT', 'Mato Grosso'),
        ('MS', 'Mato Grosso do Sul'),
        ('MG', 'Minas Gerais'),
        ('PA', 'Pará'),
        ('PB', 'Paraíba'),
        ('PR', 'Paraná'),
        ('PE', 'Pernambuco'),
        ('PI', 'Piauí'),
        ('RJ', 'Rio de Janeiro'),
        ('RN', 'Rio Grande do Norte'),
        ('RS', 'Rio Grande do Sul'),
        ('RO', 'Rondônia'),
        ('RR', 'Roraima'),
        ('SC', 'Santa Catarina'),
        ('SP', 'São Paulo'),
        ('SE', 'Sergipe'),
        ('TO', 'Tocantins'),
    ]

    logo = models.ImageField(upload_to="media/", height_field=None, width_field=None, max_length=None, null=True, blank=True)
    system_logo = models.ImageField(upload_to="media/", height_field=None, width_field=None, max_length=None, null=True, blank=True)
    name = models.CharField(max_length=200)
    cnpj = models.CharField(max_length=14, null=True, blank=True, unique=True)
    district = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    establishment_number = models.CharField(max_length=50)
    city = models.CharField(max_length=200)
    state = models.CharField(choices=STATE_CHOICES, max_length=2)
    primary_phone = models.CharField(max_length=14)
    secondary_phone = models.CharField(max_length=14, null=True, blank=True)
    email = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Company"
        verbose_name_plural = "Companies"

    def __str__(self):
        return self.name

