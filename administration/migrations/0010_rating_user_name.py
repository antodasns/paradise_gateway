# Generated by Django 2.2.3 on 2019-12-29 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0009_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='rating',
            name='user_name',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
    ]