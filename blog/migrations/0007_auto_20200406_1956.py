# Generated by Django 3.0.5 on 2020-04-06 14:26

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20200406_1724'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='publish',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 6, 14, 26, 19, 507467, tzinfo=utc)),
        ),
    ]
