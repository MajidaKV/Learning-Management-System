# Generated by Django 4.1.2 on 2022-11-24 11:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tutor', '0033_userquizanswers_delete_coursequiz'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='certificate',
            options={'verbose_name_plural': '10. Certificate'},
        ),
        migrations.AlterModelOptions(
            name='postcertificate',
            options={'verbose_name_plural': '11. postCertificate'},
        ),
        migrations.RenameField(
            model_name='postcertificate',
            old_name='certicate',
            new_name='certificate',
        ),
    ]
