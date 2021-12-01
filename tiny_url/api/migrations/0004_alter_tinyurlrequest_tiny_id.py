# Generated by Django 3.2.9 on 2021-11-30 14:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_tinyurlrequest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tinyurlrequest',
            name='tiny_id',
            field=models.ForeignKey(max_length=10, on_delete=django.db.models.deletion.CASCADE, to='api.tinyurl'),
        ),
    ]