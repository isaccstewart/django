# Generated by Django 2.1 on 2018-10-19 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtube', '0002_auto_20181019_1632'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='datetime',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
