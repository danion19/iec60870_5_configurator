# Generated by Django 2.1.5 on 2019-10-18 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0002_auto_20191018_1059'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='card',
            name='nModules',
        ),
        migrations.AlterField(
            model_name='card',
            name='type',
            field=models.TextField(default='DI16'),
        ),
    ]
