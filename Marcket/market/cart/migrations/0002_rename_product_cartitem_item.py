# Generated by Django 5.0.6 on 2024-09-07 15:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartitem',
            old_name='product',
            new_name='item',
        ),
    ]
