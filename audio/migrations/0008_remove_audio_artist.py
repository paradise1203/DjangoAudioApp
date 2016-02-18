# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audio', '0007_artist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='audio',
            name='artist',
        ),
    ]
