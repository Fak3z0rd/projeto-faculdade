# Generated by Django 4.2.4 on 2023-09-04 00:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_contaescola_is_staff'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contaescola',
            name='is_staff',
        ),
    ]
