# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='schoolrequestinformation',
            name='school_city',
            field=models.CharField(default=b'', max_length=100),
        ),
        migrations.AddField(
            model_name='schoolrequestinformation',
            name='school_postcode',
            field=models.CharField(default=b'', max_length=8),
        ),
        migrations.AlterField(
            model_name='schoolrequestinformation',
            name='chapter',
            field=models.IntegerField(default=0, choices=[(0, b'Robogals Melbourne'), (1, b'Robogals Monash (Melbourne)'), (2, b'Robogals Adelaide'), (3, b'Robogals Auckland'), (4, b'Robogals Brisbane'), (5, b'Robogals Canberra'), (6, b'Robogals Hobart'), (7, b'Robogals Newcastle'), (8, b'Robogals Perth'), (9, b'Robogals Sydney'), (10, b'Robogals Toowoomba')]),
        ),
        migrations.AlterField(
            model_name='schoolrequestinformation',
            name='first_name',
            field=models.CharField(default=b'', max_length=100),
        ),
        migrations.AlterField(
            model_name='schoolrequestinformation',
            name='last_name',
            field=models.CharField(default=b'', max_length=100),
        ),
        migrations.AlterField(
            model_name='schoolrequestinformation',
            name='mobile',
            field=models.CharField(default=b'', max_length=100),
        ),
        migrations.AlterField(
            model_name='schoolrequestinformation',
            name='school_address',
            field=models.CharField(default=b'', max_length=100),
        ),
        migrations.AlterField(
            model_name='schoolrequestinformation',
            name='school_name',
            field=models.CharField(default=b'', max_length=100),
        ),
    ]
