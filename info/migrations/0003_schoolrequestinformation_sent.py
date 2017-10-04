# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0002_auto_20171003_2219'),
    ]

    operations = [
        migrations.AddField(
            model_name='schoolrequestinformation',
            name='sent',
            field=models.BooleanField(default=0),
        ),
    ]
