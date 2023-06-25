
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Notes', '0028_alter_note_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='time',
            field=models.DateTimeField(default='2023-06-25 16:37:33'),
        ),
    ]
