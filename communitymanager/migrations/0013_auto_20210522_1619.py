# Generated by Django 2.2 on 2021-05-22 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('communitymanager', '0012_auto_20210522_1619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_evenement',
            field=models.DateTimeField(),
        ),
    ]
