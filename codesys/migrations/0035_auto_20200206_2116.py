# Generated by Django 2.1.5 on 2020-02-06 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codesys', '0034_handler'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fbdtemplate',
            old_name='InputHeader',
            new_name='FunctionBlockInputHeader',
        ),
        migrations.RenameField(
            model_name='fbdtemplate',
            old_name='OutputHeader',
            new_name='FunctionBlockOutputHeader',
        ),
        migrations.AddField(
            model_name='fbdtemplate',
            name='FunctionInputHeader',
            field=models.TextField(default=''),
        ),
    ]