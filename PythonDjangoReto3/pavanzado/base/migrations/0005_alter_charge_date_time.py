# Generated by Django 4.2.4 on 2023-08-22 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_rename_account_id_card_account_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='charge',
            name='date_time',
            field=models.DateTimeField(),
        ),
    ]
