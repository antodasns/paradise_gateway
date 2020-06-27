# Generated by Django 2.2.3 on 2019-11-19 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0006_auto_20191119_1148'),
    ]

    operations = [
        migrations.CreateModel(
            name='cab_booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cab_ref_id', models.CharField(max_length=10)),
                ('user_ref_id', models.CharField(max_length=10)),
                ('date', models.CharField(max_length=15)),
                ('time', models.CharField(max_length=15)),
                ('no_of_cab', models.CharField(max_length=10)),
                ('total_persons', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='hotel_booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hotel_ref_id', models.CharField(max_length=10)),
                ('user_ref_id', models.CharField(max_length=10)),
                ('check_in', models.CharField(max_length=15)),
                ('check_out', models.CharField(max_length=15)),
                ('no_of_rooms', models.CharField(max_length=10)),
                ('total_persons', models.CharField(max_length=10)),
            ],
        ),
    ]
