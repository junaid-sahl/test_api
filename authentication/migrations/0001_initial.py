# Generated by Django 4.1.3 on 2023-02-15 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('phone', models.CharField(blank=True, max_length=14, null=True)),
                ('password', models.CharField(max_length=255)),
                ('IsActive', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'user_account',
            },
        ),
    ]
