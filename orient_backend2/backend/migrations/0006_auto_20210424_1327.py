# Generated by Django 3.1.7 on 2021-04-24 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0005_auto_20210423_1326'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='logging',
            name='fin_hint_id',
        ),
        migrations.AddField(
            model_name='logging',
            name='reason',
            field=models.CharField(default='', max_length=1000),
        ),
    ]
