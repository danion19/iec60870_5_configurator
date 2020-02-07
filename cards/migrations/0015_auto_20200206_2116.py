# Generated by Django 2.1.5 on 2020-02-06 20:16

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0014_auto_20200130_2054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='ControlObjectList',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('obj_58c_sc_ta', 'obj_58c_sc_ta'), ('obj_59c_dc_ta', 'obj_59c_dc_ta')], max_length=27),
        ),
        migrations.AlterField(
            model_name='card',
            name='MonitorObjectList',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('obj_35m_me_te', 'obj_35m_me_te'), ('obj_31m_dp_tb', 'obj_31m_dp_tb'), ('obj_30m_sp_tb', 'obj_30m_sp_tb'), ('obj_09m_meii_na_3', 'obj_09m_meii_na_3')], max_length=59),
        ),
    ]
