# Generated by Django 2.1.5 on 2019-12-26 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server_parts', '0025_delete_obj09mmeiina3'),
    ]

    operations = [
        migrations.CreateModel(
            name='Obj59cDcTa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DeviceName', models.CharField(max_length=255)),
                ('DataType', models.CharField(choices=[('BOOL', 'BOOL'), ('WORD', 'WORD')], default='BOOL', max_length=255)),
                ('DCS', models.TextField()),
            ],
        ),
    ]
