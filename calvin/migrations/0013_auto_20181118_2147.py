# Generated by Django 2.1 on 2018-11-18 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calvin', '0012_auto_20181118_2135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='video',
            field=models.URLField(blank=True, null=True),
        ),
    ]
