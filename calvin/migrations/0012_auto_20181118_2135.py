# Generated by Django 2.1 on 2018-11-18 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calvin', '0011_page_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='video',
            field=models.URLField(blank=True),
        ),
    ]
