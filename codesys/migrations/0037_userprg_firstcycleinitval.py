# Generated by Django 2.1.5 on 2020-02-08 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codesys', '0036_userprg_programheader'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprg',
            name='FirstCycleInitVal',
            field=models.CharField(default='', max_length=255),
        ),
    ]
