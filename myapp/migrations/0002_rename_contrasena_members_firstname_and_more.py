# Generated by Django 4.1.2 on 2022-11-24 00:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='members',
            old_name='contrasena',
            new_name='firstname',
        ),
        migrations.RenameField(
            model_name='members',
            old_name='nombre',
            new_name='lastname',
        ),
    ]
