# Generated by Django 3.0.7 on 2020-06-18 05:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('problem', '0007_auto_20200214_1902'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='problem',
            options={'permissions': (('add', 'Can add problems'), ('remove', 'Can delete problems'), ('view_hidden', 'Can view hidden problems'))},
        ),
    ]