# Generated by Django 4.2.4 on 2023-08-22 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_alter_charge_date_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='open_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='payment',
            name='date_time',
            field=models.DateTimeField(),
        ),
    ]
