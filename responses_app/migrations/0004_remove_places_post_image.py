# Generated by Django 4.0.4 on 2022-06-14 19:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('responses_app', '0003_rename_file_places_post_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='places',
            name='post_image',
        ),
    ]
