# Generated by Django 3.0 on 2020-12-28 10:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_ratings_rate_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='Achievements',
            fields=[
                ('person', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('title', models.CharField(max_length=100)),
                ('details', models.CharField(max_length=4000)),
                ('achievement_pic', models.ImageField(blank=True, null=True, upload_to='pics/')),
            ],
        ),
    ]
