# Generated by Django 4.1.7 on 2023-06-25 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Notes', '0034_merge_20230625_2012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='time',
            field=models.DateTimeField(default='2023-06-25 20:24:47'),
        ),
    ]
