# Generated by Django 2.1.5 on 2019-12-01 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server_parts', '0017_auto_20191201_1355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='objsinfo',
            name='ObjCode',
            field=models.CharField(max_length=255),
        ),
    ]
