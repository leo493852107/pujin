# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-09 15:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_operation', '0002_auto_20171209_0339'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userleavingmessage',
            old_name='msg_type',
            new_name='message_type',
        ),
    ]