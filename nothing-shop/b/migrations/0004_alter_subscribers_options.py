# Generated by Django 4.0.3 on 2022-07-01 12:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('b', '0003_alter_subscribers_email_alter_subscribers_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='subscribers',
            options={'verbose_name': 'subscriber', 'verbose_name_plural': 'subscribers'},
        ),
    ]