# Generated by Django 4.1.2 on 2022-10-29 05:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_usertoken_alter_account_is_active'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='account',
            options={'verbose_name_plural': 'Students'},
        ),
    ]
