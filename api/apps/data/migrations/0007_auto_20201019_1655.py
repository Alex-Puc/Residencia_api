# Generated by Django 2.2.2 on 2020-10-19 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0006_auto_20201019_1624'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sport',
            name='training',
        ),
        migrations.AddField(
            model_name='sport',
            name='training',
            field=models.ManyToManyField(to='data.Training'),
        ),
    ]
