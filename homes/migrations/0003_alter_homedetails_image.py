# Generated by Django 5.1.1 on 2024-10-12 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homes', '0002_homedetails_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homedetails',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
    ]
