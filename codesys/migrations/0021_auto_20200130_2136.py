# Generated by Django 2.1.5 on 2020-01-30 20:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('codesys', '0020_auto_20200130_2135'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprg',
            old_name='LocalRemoteState',
            new_name='LocRemState',
        ),
        migrations.RenameField(
            model_name='userprg',
            old_name='LocalRemoteStateDataType',
            new_name='LocRemStateDataType',
        ),
        migrations.RenameField(
            model_name='userprg',
            old_name='MaskLocalRemote',
            new_name='MaskLocRem',
        ),
        migrations.RenameField(
            model_name='userprg',
            old_name='MaskLocalRemoteDataType',
            new_name='MaskLocRemDataType',
        ),
    ]
