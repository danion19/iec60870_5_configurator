# Generated by Django 2.1.5 on 2019-12-01 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server_parts', '0008_auto_20191201_0135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='ObjectList',
            field=models.CharField(choices=[('obj_35m_me_te', 'obj_35m_me_te'), ('obj_31m_dp_tb', 'obj_31m_dp_tb'), ('obj_58c_sc_ta', 'obj_58c_sc_ta')], max_length=255),
        ),
    ]
