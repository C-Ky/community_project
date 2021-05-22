# Generated by Django 2.2 on 2021-05-22 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('communitymanager', '0006_auto_20210522_1558'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='description',
            field=models.TextField(default='description of the post'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='evenementiel',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='date_evenement',
            field=models.DateTimeField(null=models.BooleanField()),
        ),
    ]