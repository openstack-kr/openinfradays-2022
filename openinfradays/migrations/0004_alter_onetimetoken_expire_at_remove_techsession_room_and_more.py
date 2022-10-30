# Generated by Django 4.1.1 on 2022-10-17 02:18

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('openinfradays', '0003_alter_onetimetoken_expire_at_remove_techsession_room_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='onetimetoken',
            name='expire_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 18, 2, 18, 28, 286175)),
        ),
        migrations.RemoveField(
            model_name='techsession',
            name='room',
        ),
        migrations.RemoveField(
            model_name='techsession',
            name='time_slot',
        ),
        migrations.AddField(
            model_name='techsession',
            name='room',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='openinfradays.room'),
        ),
        migrations.AddField(
            model_name='techsession',
            name='time_slot',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='openinfradays.timeslot'),
        ),
    ]