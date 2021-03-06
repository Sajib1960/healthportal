# Generated by Django 3.0 on 2020-12-25 18:27

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='date_of_birth',
            field=models.DateField(default=datetime.date(2020, 12, 26)),
        ),
        migrations.CreateModel(
            name='Ratings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.TextField(max_length=4000)),
                ('rating', models.CharField(choices=[(1, 'Very Bad'), (2, 'Bad'), (3, 'Average'), (4, 'Good'), (5, 'Very Good')], max_length=1)),
                ('rate_from', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rate_from', to=settings.AUTH_USER_MODEL)),
                ('rate_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rate_to', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
