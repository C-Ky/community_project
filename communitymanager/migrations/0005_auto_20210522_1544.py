# Generated by Django 2.2 on 2021-05-22 15:44

from django.db import migrations, models
import django.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('communitymanager', '0004_post_titre'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['date_creation'], 'verbose_name': 'titre'},
        ),
        migrations.AddField(
            model_name='post',
            name='date_creation',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='post',
            name='date_evenement',
            field=models.DateTimeField(null=django.db.models.fields.BooleanField),
            preserve_default=django.db.models.fields.BooleanField,
        ),
    ]