# Generated by Django 2.1.5 on 2020-02-17 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server_parts', '0029_auto_20200209_2001'),
    ]

    operations = [
        migrations.AddField(
            model_name='server',
            name='BasePort',
            field=models.CharField(default='', max_length=255),
        ),
    ]
