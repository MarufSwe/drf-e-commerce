# Generated by Django 4.2.9 on 2024-01-07 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e_products', '0006_alter_shoppingcart_products'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchase',
            name='products',
        ),
        migrations.AddField(
            model_name='purchaseitem',
            name='item_amount',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=10),
            preserve_default=False,
        ),
    ]
