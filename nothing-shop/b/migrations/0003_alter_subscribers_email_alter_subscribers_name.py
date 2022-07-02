# Generated by Django 4.0.3 on 2022-07-01 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('b', '0002_alter_subscribers_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscribers',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='subscribers',
            name='name',
            field=models.CharField(max_length=20, verbose_name='Name'),
        ),
    ]
