# Generated by Django 4.1.7 on 2023-05-08 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Notes', '0019_alter_note_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='time',
            field=models.DateTimeField(default='2023-05-08 08:06:50'),
        ),
    ]
