# Generated by Django 5.0.6 on 2024-06-04 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mahesh', '0002_computervarity_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='computervarity',
            name='description',
            field=models.TextField(default='No Description Available'),
        ),
    ]
