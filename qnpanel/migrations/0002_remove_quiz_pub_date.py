# Generated by Django 3.0.6 on 2020-05-25 17:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('qnpanel', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quiz',
            name='pub_date',
        ),
    ]
