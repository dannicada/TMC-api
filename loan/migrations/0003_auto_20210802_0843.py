# Generated by Django 3.2.5 on 2021-08-02 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loan', '0002_loan_staff'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loan',
            name='due_date',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='loan',
            name='start_date',
            field=models.DateField(blank=True),
        ),
    ]