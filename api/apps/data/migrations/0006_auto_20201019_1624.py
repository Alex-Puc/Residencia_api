# Generated by Django 2.2.2 on 2020-10-19 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0005_auto_20201019_1615'),
    ]

    operations = [
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='training',
            name='duration',
        ),
        migrations.RemoveField(
            model_name='training',
            name='repetition',
        ),
        migrations.AddField(
            model_name='training',
            name='day',
            field=models.ManyToManyField(to='data.Day'),
        ),
    ]
