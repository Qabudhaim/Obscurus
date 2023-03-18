# Generated by Django 4.1.7 on 2023-03-18 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Notes', '0009_remove_reference_link_reference_url_alter_note_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='time',
            field=models.DateTimeField(default='2023-03-18 10:14:26'),
        ),
        migrations.AlterField(
            model_name='reference',
            name='url',
            field=models.URLField(blank=True, error_messages={'invalid': 'Please enter a valid URL.', 'invalid_link': 'The provided link is invalid.'}),
        ),
    ]