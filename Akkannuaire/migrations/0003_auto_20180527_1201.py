# Generated by Django 2.0.4 on 2018-05-27 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Akkannuaire', '0002_auto_20180423_1437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consultant',
            name='telephone',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
