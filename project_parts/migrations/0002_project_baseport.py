# Generated by Django 2.1.5 on 2020-02-17 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_parts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='BasePort',
            field=models.CharField(default='', max_length=255),
        ),
    ]
