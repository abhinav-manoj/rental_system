# Generated by Django 5.1.1 on 2024-10-15 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homes', '0011_remove_homedetails_email_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='homedetails',
            name='email_id',
            field=models.EmailField(max_length=254, null=True, unique=True),
        ),
    ]
