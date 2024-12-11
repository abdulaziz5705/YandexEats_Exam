# Generated by Django 5.1.3 on 2024-12-06 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ManagerandCourierModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('role', models.CharField(choices=[('manager', 'Restaurant Manager'), ('courier', 'Courier')], default='customer', max_length=10)),
            ],
        ),
        migrations.DeleteModel(
            name='ManagerandCourier',
        ),
    ]
