# Generated by Django 3.2.5 on 2021-08-01 16:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=200, null=True)),
                ('laslt_name', models.CharField(blank=True, max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(blank=True, max_length=200)),
                ('phone_number', models.CharField(max_length=200)),
                ('occupation', models.CharField(blank=True, max_length=100)),
                ('sex', models.CharField(blank=True, max_length=10)),
                ('account_number', models.IntegerField()),
                ('bvn', models.IntegerField()),
                ('guarantor_name', models.CharField(max_length=100)),
                ('guarantor_address', models.CharField(max_length=200)),
                ('guarantor_phone_number', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'Customer',
                'verbose_name_plural': 'Customers',
            },
        ),
        migrations.CreateModel(
            name='Bussiness',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bussiness_name', models.CharField(blank=True, max_length=200)),
                ('address', models.CharField(blank=True, max_length=200)),
                ('bussiness_type', models.CharField(blank=True, max_length=100)),
                ('number_of_employees', models.IntegerField(blank=True)),
                ('bussiness_account_number', models.IntegerField(blank=True)),
                ('bvn', models.IntegerField(blank=True)),
                ('customer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='customers.customer')),
            ],
        ),
    ]
