# Generated by Django 2.2.7 on 2019-11-11 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_homepage_banner_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='info',
            field=models.CharField(max_length=140),
        ),
    ]