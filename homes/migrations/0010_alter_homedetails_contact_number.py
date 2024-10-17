# Generated by Django 5.1.1 on 2024-10-15 17:01

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homes', '0009_homedetails_contact_number_homedetails_email_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homedetails',
            name='contact_number',
            field=models.CharField(max_length=20, null=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')]),
        ),
    ]
