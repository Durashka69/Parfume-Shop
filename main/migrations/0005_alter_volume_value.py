# Generated by Django 4.0.3 on 2022-04-08 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_remove_brand_slug_remove_family_slug_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='volume',
            name='value',
            field=models.FloatField(default=0, verbose_name='Объём'),
        ),
    ]
