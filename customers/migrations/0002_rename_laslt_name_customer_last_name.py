# Generated by Django 3.2.5 on 2021-08-09 05:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='laslt_name',
            new_name='last_name',
        ),
    ]
