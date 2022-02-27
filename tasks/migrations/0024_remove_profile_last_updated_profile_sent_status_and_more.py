# Generated by Django 4.0.2 on 2022-02-27 11:10

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0023_profile_last_updated_alter_profile_alert_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='last_updated',
        ),
        migrations.AddField(
            model_name='profile',
            name='sent_status',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='profile',
            name='alert_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 27, 11, 10, 4, 292229, tzinfo=utc), null=True),
        ),
    ]
