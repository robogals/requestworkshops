# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0003_schoolrequestinformation_sent'),
    ]

    operations = [
        migrations.AddField(
            model_name='schoolrequestinformation',
            name='requested_time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
