# Generated by Django 4.0.3 on 2022-04-08 17:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_product_volume'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='brand',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='family',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='note',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='product',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='purpose',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='type_of',
            name='slug',
        ),
    ]
