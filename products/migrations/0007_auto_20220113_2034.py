# Generated by Django 3.2 on 2022-01-13 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20220113_2023'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='has_length',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='productinventory',
            name='length',
            field=models.CharField(blank=True, choices=[('S', 'Short'), ('M', 'Mid-Length'), ('L', 'Long')], max_length=2, null=True),
        ),
    ]
