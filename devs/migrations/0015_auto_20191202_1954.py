# Generated by Django 2.1.5 on 2019-12-02 18:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('devs', '0014_auto_20191201_2023'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='device',
            name='Control',
        ),
        migrations.RemoveField(
            model_name='device',
            name='Monitor',
        ),
    ]
