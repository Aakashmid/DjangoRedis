# Generated by Django 5.0.6 on 2024-06-19 14:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CacheApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Student',
            new_name='Product',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='city',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='roll_no',
            new_name='price',
        ),
    ]