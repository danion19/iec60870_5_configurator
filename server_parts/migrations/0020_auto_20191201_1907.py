# Generated by Django 2.1.5 on 2019-12-01 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server_parts', '0019_auto_20191201_1810'),
    ]

    operations = [
        migrations.AlterField(
            model_name='obj35mmete',
            name='Hysteresis',
            field=models.TextField(blank=True),
        ),
    ]
