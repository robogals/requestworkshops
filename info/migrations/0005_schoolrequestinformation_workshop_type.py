# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0004_schoolrequestinformation_requested_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='schoolrequestinformation',
            name='workshop_type',
            field=models.IntegerField(default=0, choices=[(0, b'Robotics - Robogals Workshop'), (1, b'Non-Robotics - iWorld Workshop'), (2, b'Both')]),
        ),
    ]
