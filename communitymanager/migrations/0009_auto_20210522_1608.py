# Generated by Django 2.2 on 2021-05-22 16:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('communitymanager', '0008_auto_20210522_1604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_evenement',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
