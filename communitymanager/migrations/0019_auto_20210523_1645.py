# Generated by Django 2.2 on 2021-05-23 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('communitymanager', '0018_auto_20210523_1644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_evenement',
            field=models.DateField(blank=True, null=True),
        ),
    ]
