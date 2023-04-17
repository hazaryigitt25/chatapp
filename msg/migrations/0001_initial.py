# Generated by Django 4.1.7 on 2023-04-12 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chat_name', models.CharField(max_length=15, verbose_name='Chat Name')),
                ('chat_admin', models.CharField(max_length=15, verbose_name='Chat Admin')),
                ('chat_password', models.CharField(max_length=300, verbose_name='Password')),
            ],
        ),
    ]