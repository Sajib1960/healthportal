# Generated by Django 3.0 on 2020-12-28 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0008_auto_20201228_1723'),
    ]

    operations = [
        migrations.AlterField(
            model_name='achievements',
            name='details',
            field=models.TextField(),
        ),
    ]
