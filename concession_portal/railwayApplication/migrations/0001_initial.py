# Generated by Django 2.1.5 on 2019-02-09 17:16

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RailwayApplication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_photo', models.ImageField(upload_to='railway/students/%m/%d/')),
                ('student_collegeId', models.CharField(max_length=255)),
                ('student_emailId', models.EmailField(max_length=254)),
                ('student_aadharId', models.CharField(max_length=255)),
                ('student_fullname', models.CharField(max_length=1024)),
                ('student_contact', models.CharField(max_length=100)),
                ('student_dob', models.DateField()),
                ('student_address', models.TextField()),
                ('student_bonafide', models.FileField(upload_to='bonafides/%m/%d/')),
                ('student_prevPassId', models.CharField(blank=True, max_length=255)),
                ('source_station', models.CharField(max_length=255)),
                ('destination_station', models.CharField(max_length=255)),
                ('train_class', models.CharField(choices=[('First', 'First Class'), ('Second', 'Second Class')], max_length=50)),
                ('isApproved_railway', models.BooleanField(default=False)),
                ('application_date', models.DateTimeField(default=datetime.datetime(2019, 2, 9, 17, 16, 29, 983623, tzinfo=utc))),
            ],
        ),
    ]
