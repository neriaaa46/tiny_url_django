# Generated by Django 3.2.9 on 2021-11-30 14:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_auto_20211130_1635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tinyurlrequest',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 11, 30, 16, 53, 16, 731941)),
        ),
    ]
