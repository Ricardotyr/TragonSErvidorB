# Generated by Django 4.0 on 2022-11-14 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TragonBall', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productoelaborado',
            name='precioventa',
            field=models.CharField(db_column='PrecioVenta', max_length=50),
        ),
    ]
