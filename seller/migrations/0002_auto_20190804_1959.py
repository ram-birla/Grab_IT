# Generated by Django 2.2.4 on 2019-08-04 19:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=20, unique=True)),
                ('count', models.IntegerField(default=0)),
            ],
        ),
        migrations.AlterField(
            model_name='seller',
            name='contact',
            field=models.IntegerField(default=0),
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=20, unique=True)),
                ('count', models.IntegerField(default=0)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seller.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=20)),
                ('price', models.IntegerField(default=100)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seller.Category')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seller.Seller')),
                ('subcategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seller.SubCategory')),
            ],
        ),
    ]