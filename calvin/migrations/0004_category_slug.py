# Generated by Django 2.1 on 2018-11-14 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calvin', '0003_auto_20181112_1617'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default='', unique=True),
            preserve_default=False,
        ),
    ]
