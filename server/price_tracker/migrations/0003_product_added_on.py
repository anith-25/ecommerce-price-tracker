# Generated by Django 4.2 on 2023-05-01 08:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('price_tracker', '0002_alter_product_current_price_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='added_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
