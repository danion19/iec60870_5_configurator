# Generated by Django 2.1.5 on 2020-02-03 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codesys', '0029_auto_20200203_2016'),
    ]

    operations = [
        migrations.AddField(
            model_name='save',
            name='Reason',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='save',
            name='ReasonDataType',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='save',
            name='ReasonInitVal',
            field=models.CharField(default='', max_length=255),
        ),
    ]