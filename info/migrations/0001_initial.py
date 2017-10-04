# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SchoolRequestInformation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('school_name', models.CharField(max_length=100)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('mobile', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('school_address', models.CharField(max_length=100)),
                ('position', models.CharField(max_length=100)),
                ('chapter', models.IntegerField(choices=[(0, b'Robogals Melbourne'), (1, b'Robogals Monash (Melbourne)'), (2, b'Robogals Adelaide'), (3, b'Robogals Auckland'), (4, b'Robogals Brisbane'), (5, b'Robogals Canberra'), (6, b'Robogals Hobart'), (7, b'Robogals Newcastle'), (8, b'Robogals Perth'), (9, b'Robogals Sydney'), (10, b'Robogals Toowoomba')])),
                ('permission_to_contact', models.BooleanField(default=0)),
            ],
        ),
    ]
