# Generated by Django 2.1.5 on 2020-02-10 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codesys', '0041_auto_20200210_1537'),
    ]

    operations = [
        migrations.CreateModel(
            name='CheckLocRem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Version', models.CharField(max_length=255)),
                ('Iterator', models.CharField(default='', max_length=255)),
                ('IteratorDataType', models.CharField(default='', max_length=255)),
                ('ST', models.TextField(default='')),
            ],
        ),
    ]
