# Generated by Django 3.2.4 on 2021-06-21 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20210621_1506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userbias',
            name='bias',
            field=models.FloatField(default=0),
        ),
    ]
