# Generated by Django 2.1.5 on 2020-01-07 15:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('codesys', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='map',
            old_name='Variable_Declaration',
            new_name='VariableDeclaration',
        ),
    ]
