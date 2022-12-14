# Generated by Django 4.1.1 on 2022-10-17 01:30

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('openinfradays', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='TimeSlot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.CharField(max_length=10)),
                ('end_time', models.CharField(max_length=10)),
            ],
        ),
        migrations.AlterField(
            model_name='onetimetoken',
            name='expire_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 18, 1, 30, 20, 639508)),
        ),
        migrations.AlterField(
            model_name='techsession',
            name='details',
            field=models.TextField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='techsession',
            name='session_type',
            field=models.CharField(choices=[('Keynote', 'Keynote'), ('Sponsor', 'Sponsor'), ('Tech', 'Tech'), ('Community', 'Community'), ('Online', 'Online')], default='Tech', max_length=20),
        ),
        migrations.AddField(
            model_name='techsession',
            name='room',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='openinfradays.room'),
        ),
        migrations.AddField(
            model_name='techsession',
            name='time_slot',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='openinfradays.timeslot'),
        ),
    ]
