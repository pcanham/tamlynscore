# Generated by Django 4.2.6 on 2023-10-21 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entries', '0037_entry_users'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entryuser',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
