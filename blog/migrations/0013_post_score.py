# Generated by Django 3.1 on 2022-11-26 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20221126_1947'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='score',
            field=models.IntegerField(default=10),
        ),
    ]
