# Generated by Django 3.1.3 on 2020-11-25 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_account_nav_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='nav_color',
            field=models.TextField(blank=True, null=True),
        ),
    ]
