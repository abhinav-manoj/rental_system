# Generated by Django 5.1.1 on 2024-10-17 05:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homes', '0012_homedetails_email_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='state',
            name='master_ptr',
        ),
        migrations.DeleteModel(
            name='Master',
        ),
        migrations.DeleteModel(
            name='State',
        ),
    ]
