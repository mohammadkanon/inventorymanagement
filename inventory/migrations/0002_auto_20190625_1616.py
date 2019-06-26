# Generated by Django 2.2.2 on 2019-06-25 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='desktop',
            name='status',
            field=models.CharField(choices=[('AVAILABLE', 'Item is ready to purchased'), ('SOLD', 'Item sold'), ('RESTOCKING', 'Item restocking in few days')], default='Sold', max_length=10),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='status',
            field=models.CharField(choices=[('AVAILABLE', 'Item is ready to purchased'), ('SOLD', 'Item sold'), ('RESTOCKING', 'Item restocking in few days')], default='Sold', max_length=10),
        ),
        migrations.AlterField(
            model_name='mobile',
            name='status',
            field=models.CharField(choices=[('AVAILABLE', 'Item is ready to purchased'), ('SOLD', 'Item sold'), ('RESTOCKING', 'Item restocking in few days')], default='Sold', max_length=10),
        ),
    ]
