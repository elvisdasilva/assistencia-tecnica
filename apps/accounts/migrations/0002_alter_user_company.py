# Generated by Django 5.1.2 on 2024-10-30 00:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('companies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='companies.company', verbose_name='Company'),
        ),
    ]