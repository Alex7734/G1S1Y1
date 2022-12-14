# Generated by Django 4.1.3 on 2022-11-27 05:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0017_alter_feedback_date_posted_alter_post_date_posted"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="name",
            field=models.TextField(default="", max_length=512),
        ),
        migrations.AlterField(
            model_name="feedback",
            name="date_posted",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2022, 11, 27, 5, 25, 41, 691809, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="date_posted",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2022, 11, 27, 5, 25, 41, 691809, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
