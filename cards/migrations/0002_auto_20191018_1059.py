# Generated by Django 2.1.5 on 2019-10-18 08:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='card',
            old_name='nModuls',
            new_name='nModules',
        ),
    ]
