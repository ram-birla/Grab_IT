# Generated by Django 2.2.4 on 2019-08-12 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0006_pcount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, default='', null=True, upload_to='shop/images'),
        ),
    ]