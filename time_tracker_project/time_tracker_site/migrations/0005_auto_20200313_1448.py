# Generated by Django 2.2 on 2020-03-13 14:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('time_tracker_site', '0004_auto_20200313_1411'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timetracking',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,
                                    to=settings.AUTH_USER_MODEL),
        ),
    ]
