# Generated by Django 4.0.4 on 2022-06-09 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('responses_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='texttt',
        ),
        migrations.AddField(
            model_name='places',
            name='file',
            field=models.ImageField(null=True, upload_to='files/'),
        ),
    ]
