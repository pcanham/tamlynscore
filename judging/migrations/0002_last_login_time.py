# Generated by Django 4.2.6 on 2023-10-21 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('judging', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='judge',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
