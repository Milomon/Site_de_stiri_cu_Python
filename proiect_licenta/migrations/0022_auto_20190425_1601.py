# Generated by Django 2.1.7 on 2019-04-25 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proiect_licenta', '0021_auto_20190425_1556'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image_title',
            field=models.ImageField(default='pamant.jpg', upload_to=''),
        ),
    ]
