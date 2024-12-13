# Generated by Django 5.1.3 on 2024-12-12 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='managerandcouriermodel',
            name='first_name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='managerandcouriermodel',
            name='last_name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='managerandcouriermodel',
            name='role',
            field=models.CharField(choices=[('manager', 'Restaurant Manager'), ('courier', 'Courier')], default='courier', max_length=255),
        ),
        migrations.AlterField(
            model_name='managerandcouriermodel',
            name='username',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]