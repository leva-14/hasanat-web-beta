# Generated by Django 3.1.2 on 2020-12-24 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0005_auto_20201224_1028'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='img_2',
            field=models.ImageField(default='', upload_to='Projects_images/'),
        ),
    ]