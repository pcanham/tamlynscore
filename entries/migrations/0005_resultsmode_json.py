# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('entries', '0004_auto_20150528_2034'),
    ]

    operations = [
        migrations.AddField(
            model_name='resultsmode',
            name='json',
            field=models.TextField(default=b'', editable=False, blank=True),
        ),
    ]
