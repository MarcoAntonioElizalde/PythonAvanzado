# Generated by Django 4.2.4 on 2023-08-22 18:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_rename_accountnumber_account_account_number'),
    ]

    operations = [
        migrations.RenameField(
            model_name='card',
            old_name='account_id',
            new_name='account_number',
        ),
    ]
