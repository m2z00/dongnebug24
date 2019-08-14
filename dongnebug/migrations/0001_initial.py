# Generated by Django 2.2.4 on 2019-08-12 17:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Complain',
            fields=[
                ('author', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('title', models.TextField()),
                ('content', models.TextField()),
                ('latitude', models.IntegerField(default=0)),
                ('longitude', models.IntegerField(default=0)),
                ('num_of_sympathies', models.IntegerField(default=0)),
                ('num_of_comments', models.IntegerField(default=0)),
                ('is_complete', models.BooleanField(default=False)),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Sympathy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('complain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dongnebug.Complain')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('complain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dongnebug.Complain')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ComplainImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='')),
                ('complain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dongnebug.Complain')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('complain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dongnebug.Complain')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
