# Generated by Django 2.2.7 on 2020-02-02 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0014_auto_20200129_2113'),
    ]

    operations = [
        migrations.AddField(
            model_name='place_details',
            name='kilometers_more',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
    ]
