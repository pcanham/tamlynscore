# Generated by Django 4.0.6 on 2022-10-04 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_wa_age_group_changes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='archer',
            name='gender',
            field=models.CharField(choices=[('G', 'Men'), ('L', 'Women')], max_length=1),
        ),
    ]
