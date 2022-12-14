# Generated by Django 4.1.1 on 2022-09-11 17:04

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AdVideo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Bof',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=100)),
                ('moderator', models.CharField(default='', max_length=120)),
                ('profile_img', models.ImageField(blank=True, default=None, upload_to='images/bof/')),
                ('bof_date', models.DateField(default='2021-12-07')),
                ('bof_time', models.CharField(default='', max_length=30)),
                ('content', models.TextField(default='', max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Speaker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('company', models.CharField(default='', max_length=100)),
                ('profile_img', models.ImageField(blank=True, default=None, upload_to='images/speaker/')),
                ('bio', models.TextField(default='', max_length=1000)),
                ('twitter', models.CharField(blank=True, default='', max_length=100)),
                ('facebook', models.CharField(blank=True, default='', max_length=100)),
                ('blog', models.CharField(blank=True, default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Sponsor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_ko', models.CharField(default='', max_length=100)),
                ('name_en', models.CharField(max_length=100)),
                ('homepage_url', models.CharField(default='', max_length=100)),
                ('logo', models.ImageField(upload_to='images/sponsor/')),
                ('level', models.CharField(choices=[('Diamond', 'Diamond'), ('Sapphire', 'Sapphire'), ('Gold', 'Gold'), ('Media', 'Media')], default='Gold', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='VirtualBooth',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, default='', max_length=200)),
                ('short_desc', models.CharField(blank=True, default='', max_length=200)),
                ('body', models.TextField(blank=True, default='', max_length=10000)),
                ('custom_logo', models.ImageField(blank=True, default=None, null=True, upload_to='images/virtualbooth/')),
                ('video1', models.CharField(blank=True, default='', max_length=100)),
                ('video2', models.CharField(blank=True, default='', max_length=100)),
                ('video3', models.CharField(blank=True, default='', max_length=100)),
                ('image1', models.ImageField(blank=True, default=None, upload_to='images/virtualbooth/')),
                ('image1_link', models.FileField(blank=True, default='', upload_to='files/virtualbooth/')),
                ('image2', models.ImageField(blank=True, default=None, upload_to='images/virtualbooth/')),
                ('image2_link', models.FileField(blank=True, default='', upload_to='files/virtualbooth/')),
                ('image3', models.ImageField(blank=True, default=None, upload_to='images/virtualbooth/')),
                ('link1', models.CharField(blank=True, default='', max_length=100)),
                ('link1_txt', models.CharField(blank=True, default='', max_length=100)),
                ('link2', models.CharField(blank=True, default='', max_length=100)),
                ('link2_txt', models.CharField(blank=True, default='', max_length=100)),
                ('link3', models.CharField(blank=True, default='', max_length=100)),
                ('link3_txt', models.CharField(blank=True, default='', max_length=100)),
                ('link4', models.CharField(blank=True, default='', max_length=100)),
                ('link4_txt', models.CharField(blank=True, default='', max_length=100)),
                ('link5', models.CharField(blank=True, default='', max_length=100)),
                ('link5_txt', models.CharField(blank=True, default='', max_length=100)),
                ('sponsor', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='openinfradays.sponsor')),
            ],
        ),
        migrations.CreateModel(
            name='TechSession',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('details', models.TextField(max_length=1000)),
                ('slide', models.FileField(blank=True, default='', upload_to='slides/')),
                ('video_url', models.CharField(blank=True, default='', max_length=1000)),
                ('ad1_url', models.CharField(blank=True, default='', max_length=1000)),
                ('ad2_url', models.CharField(blank=True, default='', max_length=1000)),
                ('open_date', models.DateField(default='2021-12-07')),
                ('session_type', models.CharField(choices=[('Keynote', 'Keynote'), ('Sponsor', 'Sponsor'), ('Tech', 'Tech'), ('Community', 'Community')], default='Tech', max_length=20)),
                ('qna_enable', models.BooleanField(blank=True, default=False)),
                ('qna_date', models.DateField(blank=True, default='2021-12-07')),
                ('qna_time', models.TimeField(blank=True, default='00:00:00')),
                ('qna_location', models.CharField(default='Gather Town', max_length=100)),
                ('speaker', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='openinfradays.speaker')),
            ],
        ),
        migrations.CreateModel(
            name='SponsorNight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_date', models.DateField(blank=True, default='2021-12-07')),
                ('event_time', models.CharField(blank=True, default='', max_length=100)),
                ('feature1', models.CharField(blank=True, default='', max_length=100)),
                ('feature2', models.CharField(blank=True, default='', max_length=100)),
                ('feature3', models.CharField(blank=True, default='', max_length=100)),
                ('custom_btn_txt', models.CharField(blank=True, default='', max_length=100)),
                ('custom_btn_link', models.CharField(blank=True, default='', max_length=100)),
                ('sponsor', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='openinfradays.sponsor')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_check_navercloud', models.BooleanField(default=False)),
                ('login_type', models.CharField(max_length=10)),
                ('complete', models.BooleanField(default=False)),
                ('company', models.CharField(blank=True, default='', max_length=100)),
                ('job', models.CharField(blank=True, default='', max_length=100)),
                ('agree_with_private', models.BooleanField(default=False, null=True)),
                ('agree_with_sponsor', models.BooleanField(default=False, null=True)),
                ('naver_cloud_form', models.CharField(blank=True, default='', max_length=10000)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OnetimeToken',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(blank=True, default='', max_length=100)),
                ('expired', models.BooleanField(default=False)),
                ('error_msg', models.CharField(blank=True, default='', max_length=10000)),
                ('request_ip', models.CharField(blank=True, default='', max_length=100)),
                ('access_time', models.DateTimeField(null=True)),
                ('expire_at', models.DateTimeField(default=datetime.datetime(2022, 9, 12, 17, 4, 49, 369157))),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
