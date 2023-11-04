# Generated by Django 4.2.6 on 2023-11-04 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entries', '0039_make_on_device_optional'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='scoring_system',
            field=models.CharField(choices=[('F', 'Full running slips'), ('D', 'Dozen running slips'), ('T', 'Totals only'), ('A', 'On archer mobile devices')], max_length=1),
        ),
    ]
