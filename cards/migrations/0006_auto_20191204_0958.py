# Generated by Django 2.1.5 on 2019-12-04 08:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0005_auto_20191201_2023'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='card',
            name='Control',
        ),
        migrations.RemoveField(
            model_name='card',
            name='IO',
        ),
        migrations.RemoveField(
            model_name='card',
            name='Monitor',
        ),
    ]
