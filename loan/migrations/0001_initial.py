# Generated by Django 3.2.5 on 2021-08-01 16:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(blank=True, decimal_places=10, max_digits=19)),
                ('repayment_amount', models.DecimalField(blank=True, decimal_places=10, max_digits=19)),
                ('interest', models.DecimalField(blank=True, decimal_places=10, max_digits=19)),
                ('repaid', models.BooleanField(default=False)),
                ('approved', models.BooleanField(default=False)),
                ('start_date', models.DateField()),
                ('due_date', models.DateField()),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='customers.customer')),
            ],
            options={
                'verbose_name': 'Loan',
                'verbose_name_plural': 'Loans',
            },
        ),
    ]
