# Generated by Django 4.1.7 on 2023-03-18 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Notes', '0013_alter_note_time_alter_reference_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='time',
            field=models.DateTimeField(default='2023-03-18 12:09:48'),
        ),
    ]
