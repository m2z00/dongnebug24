# Generated by Django 2.2.4 on 2019-08-12 15:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dongnebug', '0003_auto_20190811_2201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complain',
            name='author',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]
