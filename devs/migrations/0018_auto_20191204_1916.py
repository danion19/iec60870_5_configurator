# Generated by Django 2.1.5 on 2019-12-04 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devs', '0017_auto_20191204_1857'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='Protocol',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='device',
            name='Server',
            field=models.CharField(choices=[('yes', 'yes'), ('no', 'no')], default='yes', max_length=255),
        ),
    ]
