# Generated by Django 5.2.4 on 2025-07-17 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_alter_project_options_project_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='projectImg_relative',
            field=models.ImageField(null=True, upload_to='projects/relative_img'),
        ),
        migrations.AlterField(
            model_name='project',
            name='projectImg_big',
            field=models.ImageField(null=True, upload_to='projects/big_img/'),
        ),
        migrations.AlterField(
            model_name='project',
            name='projectImg_small',
            field=models.ImageField(null=True, upload_to='projects/small_img/'),
        ),
    ]
