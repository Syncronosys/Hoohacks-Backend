# Generated by Django 3.1.7 on 2021-03-28 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='uuid',
            field=models.CharField(default='8d6955aa', max_length=8),
        ),
    ]
