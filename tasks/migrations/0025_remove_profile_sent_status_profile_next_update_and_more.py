# Generated by Django 4.0.2 on 2022-02-27 12:32

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0024_remove_profile_last_updated_profile_sent_status_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='sent_status',
        ),
        migrations.AddField(
            model_name='profile',
            name='next_update',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='alert_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 27, 12, 32, 40, 895446, tzinfo=utc), null=True),
        ),
    ]