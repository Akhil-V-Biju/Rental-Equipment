# Generated by Django 4.2.7 on 2024-03-25 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipment_app', '0013_alter_buy_cart_prof'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buy_cart',
            name='prof',
            field=models.ImageField(blank=True, null=True, upload_to='product_image/'),
        ),
    ]
