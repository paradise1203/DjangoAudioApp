# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audio', '0008_remove_audio_artist'),
    ]

    operations = [
        migrations.AddField(
            model_name='audio',
            name='artist',
            field=models.ForeignKey(to='audio.Artist', null=True),
        ),
    ]
