# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JobSeeker',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, null=True, blank=True)),
                ('gender', models.CharField(blank=True, max_length=200, null=True, choices=[(b'Male', b'Male'), (b'Female', b'Female')])),
                ('resume', models.FileField(upload_to=b'')),
                ('college', models.CharField(max_length=200, null=True, blank=True)),
                ('year_in_college', models.CharField(blank=True, max_length=200, null=True, choices=[(b'Freshman', b'Freshman'), (b'Sophomore', b'Sophomore'), (b'Junior', b'Junior'), (b'Senior', b'Senior'), (b'Graduated', b'Graduated'), (b'Not_in_college', b'Not In College')])),
                ('college_email', models.EmailField(max_length=200, null=True, blank=True)),
                ('positions_interested_in', models.CharField(max_length=200, choices=[(b'Campus Ambassador', b'Campus Ambassador')])),
                ('affiliated_with_greek_life', models.CharField(max_length=200, null=True, blank=True)),
                ('why_groupster', models.CharField(max_length=200, null=True, blank=True)),
                ('skills', models.CharField(max_length=200, null=True, blank=True)),
                ('why_hire', models.CharField(max_length=200, null=True, blank=True)),
            ],
        ),
    ]
