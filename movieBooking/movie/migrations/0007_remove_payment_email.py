# Generated by Django 5.0.1 on 2024-02-01 03:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0006_alter_payment_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='email',
        ),
    ]