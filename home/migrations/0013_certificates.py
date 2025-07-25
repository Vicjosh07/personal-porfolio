# Generated by Django 5.2.4 on 2025-07-19 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_delete_certificates'),
    ]

    operations = [
        migrations.CreateModel(
            name='Certificates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('company_name', models.CharField(max_length=100, null=True)),
                ('company_location', models.CharField(max_length=100, null=True)),
                ('company_logo', models.ImageField(null=True, upload_to='certificates/logo/')),
                ('certificateImg_small', models.ImageField(null=True, upload_to='certificates/small_img/')),
                ('certificateImg_big', models.ImageField(null=True, upload_to='certificates/big_img/')),
            ],
            options={
                'verbose_name': '6. Certificates',
                'verbose_name_plural': '6. Certificates',
            },
        ),
    ]
