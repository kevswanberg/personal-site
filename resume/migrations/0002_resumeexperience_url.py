# Generated by Django 2.2.7 on 2019-11-23 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='resumeexperience',
            name='url',
            field=models.URLField(null=True),
        ),
    ]
