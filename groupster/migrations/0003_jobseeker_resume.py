# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('groupster', '0002_remove_jobseeker_resume'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobseeker',
            name='resume',
            field=models.FileField(default=None, upload_to=b''),
        ),
    ]
