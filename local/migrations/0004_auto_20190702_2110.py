# Generated by Django 2.2.2 on 2019-07-03 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('local', '0003_auto_20190623_0147'),
    ]

    operations = [
        migrations.AddField(
            model_name='courtsoccer',
            name='end_time',
            field=models.TimeField(null=True),
        ),
        migrations.AddField(
            model_name='courtsoccer',
            name='start_time',
            field=models.TimeField(null=True),
        ),
    ]
