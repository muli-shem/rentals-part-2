# Generated by Django 5.0.2 on 2024-02-22 07:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('useraccount', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='Phone',
        ),
    ]
