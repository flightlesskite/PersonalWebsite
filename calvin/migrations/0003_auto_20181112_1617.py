# Generated by Django 2.1 on 2018-11-12 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calvin', '0002_auto_20181111_1649'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='likes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='category',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]
