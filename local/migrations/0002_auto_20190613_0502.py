# Generated by Django 2.2.2 on 2019-06-13 05:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('local', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='local',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_local', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='gallery',
            name='court_soccer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='court_soccer_gallery', to='local.CourtSoccer'),
        ),
        migrations.AddField(
            model_name='courtsoccer',
            name='local',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='local_court_soccer', to='local.Local'),
        ),
    ]
