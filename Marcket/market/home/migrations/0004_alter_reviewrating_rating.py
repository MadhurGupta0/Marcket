# Generated by Django 5.0.6 on 2024-09-07 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_reviewrating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviewrating',
            name='rating',
            field=models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=0),
        ),
    ]
