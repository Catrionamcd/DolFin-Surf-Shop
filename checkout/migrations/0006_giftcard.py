# Generated by Django 3.2 on 2022-01-23 16:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0005_order_user_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='GiftCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('giftcard_code', models.CharField(editable=False, max_length=8)),
                ('giftcard_value', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('giftcard_value_remaining', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('order_line_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Giftcards', to='checkout.orderlineitem')),
            ],
        ),
    ]
