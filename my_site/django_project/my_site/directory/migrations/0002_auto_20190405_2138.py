# Generated by Django 2.2 on 2019-04-05 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('directory', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='name',
            field=models.CharField(max_length=30, verbose_name='имя автора'),
        ),
    ]
