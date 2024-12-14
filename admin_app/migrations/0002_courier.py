# Generated by Django 5.1.3 on 2024-12-14 08:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Courier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='courier', to='admin_app.managerandcouriermodel')),
            ],
            options={
                'verbose_name': 'Courier',
                'verbose_name_plural': 'Couriers',
                'db_table': 'courier',
            },
        ),
    ]