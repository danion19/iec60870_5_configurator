# Generated by Django 2.1.5 on 2020-01-07 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codesys', '0004_check'),
    ]

    operations = [
        migrations.CreateModel(
            name='Save',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Version', models.CharField(max_length=255)),
                ('VariableDeclaration', models.TextField(default='')),
                ('Code', models.TextField(default='')),
            ],
        ),
    ]
