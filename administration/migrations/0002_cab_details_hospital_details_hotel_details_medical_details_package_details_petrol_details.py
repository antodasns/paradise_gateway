# Generated by Django 2.2.3 on 2019-11-11 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='cab_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cabname', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=30)),
                ('location', models.CharField(max_length=30)),
                ('pincode', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='hospital_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hospitalname', models.CharField(max_length=30)),
                ('location', models.CharField(max_length=30)),
                ('pincode', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='hotel_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hotelname', models.CharField(max_length=30)),
                ('location', models.CharField(max_length=30)),
                ('pincode', models.CharField(max_length=30)),
                ('roomsavailable', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='medical_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('location', models.CharField(max_length=30)),
                ('pincode', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='package_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('package_name', models.CharField(max_length=30)),
                ('place', models.CharField(max_length=30)),
                ('location', models.CharField(max_length=30)),
                ('pincode', models.CharField(max_length=30)),
                ('starttime', models.CharField(max_length=30)),
                ('endtime', models.CharField(max_length=30)),
                ('breakfasttime', models.CharField(max_length=30)),
                ('lunchtime', models.CharField(max_length=30)),
                ('teatime', models.CharField(max_length=30)),
                ('dinnertime', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='petrol_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('location', models.CharField(max_length=30)),
                ('pincode', models.CharField(max_length=30)),
            ],
        ),
    ]
