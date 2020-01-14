# Generated by Django 2.1.5 on 2019-12-05 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devs', '0021_remove_device_client'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='device',
            name='ClientControlObjectList',
        ),
        migrations.RemoveField(
            model_name='device',
            name='ClientMonitorObjectList',
        ),
        migrations.AddField(
            model_name='device',
            name='ClientObjs',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='device',
            name='ClientSignals',
            field=models.TextField(blank=True),
        ),
    ]
