# Generated by Django 4.2.1 on 2024-04-09 19:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_brand_product_is_active_product_liked_users_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='product.category', verbose_name='Category'),
        ),
    ]
