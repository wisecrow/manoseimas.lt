# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mps_v2', '0008_groupranking_mpranking'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groupmembership',
            name='member',
            field=models.ForeignKey(related_name='memberships', to='mps_v2.ParliamentMember'),
        ),
    ]
