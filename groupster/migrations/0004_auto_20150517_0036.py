# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('groupster', '0003_jobseeker_resume'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobseeker',
            name='resume',
            field=models.FileField(null=True, upload_to=b'', blank=True),
        ),
    ]
