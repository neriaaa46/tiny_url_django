# Generated by Django 3.2.9 on 2021-11-30 16:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_rename_tiny_id_tinyurlrequest_tiny_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tinyurlrequest',
            name='date',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]
