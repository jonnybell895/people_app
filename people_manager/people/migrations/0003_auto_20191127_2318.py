# Generated by Django 2.2.7 on 2019-11-27 23:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0002_auto_20191125_2259'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='people',
            options={'ordering': ['name', 'email']},
        ),
    ]
