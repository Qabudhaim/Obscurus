# Generated by Django 4.1.7 on 2023-06-25 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Notes', '0004_alter_note_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='time',
            field=models.DateTimeField(default='2023-06-25 21:45:40'),
        ),
    ]