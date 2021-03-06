# Generated by Django 3.1.7 on 2021-03-28 07:49

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20210328_0301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='anger',
            field=models.DecimalField(decimal_places=10, default=0.0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='client',
            name='contempt',
            field=models.DecimalField(decimal_places=10, default=0.0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='client',
            name='disgust',
            field=models.DecimalField(decimal_places=10, default=0.0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='client',
            name='fear',
            field=models.DecimalField(decimal_places=10, default=0.0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='client',
            name='happiness',
            field=models.DecimalField(decimal_places=10, default=0.0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='client',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='client',
            name='neutral',
            field=models.DecimalField(decimal_places=10, default=0.0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='client',
            name='sadness',
            field=models.DecimalField(decimal_places=10, default=0.0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='client',
            name='surprise',
            field=models.DecimalField(decimal_places=10, default=0.0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='client',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('76f36f60-b794-4f1e-b9b1-dcc7adabf71d')),
        ),
        migrations.AlterField(
            model_name='session',
            name='uuid',
            field=models.CharField(default='c9781a7f', max_length=8),
        ),
    ]
