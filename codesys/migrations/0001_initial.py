# Generated by Django 2.1.5 on 2020-01-07 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Map',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Version', models.CharField(max_length=255)),
                ('Variable_Declaration', models.TextField(default='')),
                ('Code', models.TextField(default='')),
            ],
        ),
    ]
