# Generated by Django 2.1 on 2018-11-22 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calvin', '0015_category_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]