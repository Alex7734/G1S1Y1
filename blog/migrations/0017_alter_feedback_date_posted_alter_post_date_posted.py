# Generated by Django 4.1.3 on 2022-11-27 01:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0016_alter_post_date_posted_feedback"),
    ]

    operations = [
        migrations.AlterField(
            model_name="feedback",
            name="date_posted",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2022, 11, 27, 1, 45, 53, 529303, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="date_posted",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2022, 11, 27, 1, 45, 53, 528303, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
