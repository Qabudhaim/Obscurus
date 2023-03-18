# Generated by Django 4.1.7 on 2023-03-18 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Notes', '0008_alter_note_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reference',
            name='link',
        ),
        migrations.AddField(
            model_name='reference',
            name='url',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='note',
            name='time',
            field=models.DateTimeField(default='2023-03-18 10:07:32'),
        ),
    ]
