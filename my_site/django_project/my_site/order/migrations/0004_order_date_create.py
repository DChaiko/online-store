# Generated by Django 2.2 on 2019-05-21 18:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_auto_20190521_2030'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='date_create',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Дата создания'),
            preserve_default=False,
        ),
    ]