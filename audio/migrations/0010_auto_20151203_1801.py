# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audio', '0009_audio_artist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='name',
            field=models.CharField(unique=True, max_length=50),
        ),
    ]
