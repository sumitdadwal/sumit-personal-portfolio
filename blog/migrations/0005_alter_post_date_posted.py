# Generated by Django 3.2.7 on 2021-09-15 19:21

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_post_date_posted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 15, 19, 21, 12, 259889, tzinfo=utc)),
        ),
    ]
