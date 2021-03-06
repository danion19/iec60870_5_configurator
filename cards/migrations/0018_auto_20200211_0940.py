# Generated by Django 2.1.5 on 2020-02-11 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0017_remove_card_protocol'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='card',
            name='KbusInfo',
        ),
        migrations.RemoveField(
            model_name='card',
            name='Name',
        ),
        migrations.AddField(
            model_name='card',
            name='ArticleNo',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='card',
            name='IO',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='card',
            name='ModuleChannels',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='card',
            name='ModuleType',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='card',
            name='SubBusName',
            field=models.CharField(default='', max_length=255),
        ),
    ]
