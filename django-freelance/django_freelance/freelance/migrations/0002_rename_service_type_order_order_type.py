# Generated by Django 4.1.7 on 2023-02-20 19:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('freelance', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='service_type',
            new_name='order_type',
        ),
    ]
