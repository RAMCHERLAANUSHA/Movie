# Generated by Django 5.0.1 on 2024-02-01 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0008_payment_email_payment_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='payment',
            name='password',
            field=models.CharField(max_length=10),
        ),
    ]
