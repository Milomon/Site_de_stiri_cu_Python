# Generated by Django 2.1.7 on 2019-06-10 12:34

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('proiect_licenta', '0033_auto_20190531_1735'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='likes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='post',
            name='categories',
            field=models.CharField(choices=[('FOTBAL', 'Fotbal'), ('TENIS', 'Tenis'), ('STIRI_EXTERNE', 'Stiri externe'), ('HANDBAL', 'Handbal'), ('BASKET', 'Basket'), ('ALTE_SPORTURI', 'Alte sporturi')], default='Fotbal', max_length=200),
        ),
    ]
