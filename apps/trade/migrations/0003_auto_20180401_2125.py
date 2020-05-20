# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-04-01 21:25
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0003_auto_20180113_2129'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('trade', '0002_auto_20171209_0339'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='shoppingcart',
            unique_together=set([('user', 'goods')]),
        ),
    ]