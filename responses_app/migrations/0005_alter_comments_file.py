# Generated by Django 4.0.4 on 2022-06-23 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('responses_app', '0004_remove_places_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='file',
            field=models.ImageField(blank=True, null=True, upload_to='files/'),
        ),
    ]
