# Generated by Django 5.2.4 on 2025-07-19 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_certificates'),
    ]

    operations = [
        migrations.AddField(
            model_name='certificates',
            name='certificate_url',
            field=models.URLField(null=True),
        ),
    ]
