# Generated by Django 2.2.7 on 2019-11-21 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0003_auto_20191117_1143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socialmedialink',
            name='platform_name',
            field=models.CharField(choices=[('at', 'Email'), ('github', 'Github'), ('stack-overflow', 'Stack Overflow'), ('facebook', 'Facebook'), ('twitter', 'Twitter')], max_length=100),
        ),
    ]
