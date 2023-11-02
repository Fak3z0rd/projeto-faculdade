# Generated by Django 4.2.4 on 2023-11-02 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('app', '0015_alter_acessoaluno_groups_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='acessoaluno',
            name='groups',
            field=models.ManyToManyField(blank=True, related_name='acessoaluno_user_set', to='auth.group'),
        ),
        migrations.AlterField(
            model_name='acessoaluno',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, related_name='acessoaluno_user_set', to='auth.permission'),
        ),
    ]