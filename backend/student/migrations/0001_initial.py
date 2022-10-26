# Generated by Django 4.1.2 on 2022-10-21 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('mobile', models.CharField(max_length=10, null=True, unique=True)),
                ('password', models.CharField(max_length=220)),
                ('qualification', models.CharField(max_length=220)),
                ('dp', models.ImageField(blank=True, upload_to='photos/users_dp/')),
                ('bio', models.TextField(blank=True, null=True)),
                ('interests', models.TextField(blank=True, max_length=1000, null=True)),
                ('wallet_balance', models.IntegerField(default=0)),
                ('account_holder_name', models.CharField(blank=True, max_length=200, null=True)),
                ('bank', models.CharField(blank=True, max_length=200, null=True)),
                ('acc', models.CharField(blank=True, max_length=20, null=True)),
                ('ifsc', models.CharField(blank=True, max_length=20, null=True)),
                ('courses_created', models.IntegerField(default=0)),
                ('courses_enrolled', models.IntegerField(default=0)),
                ('joined_date', models.DateTimeField(auto_now_add=True)),
                ('last_login', models.DateTimeField(auto_now=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_verified', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
