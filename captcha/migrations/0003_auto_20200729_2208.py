# Generated by Django 3.1rc1 on 2020-07-29 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('captcha', '0002_auto_20200615_1842'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='captchastore',
            name='expire_time',
        ),
        migrations.AddField(
            model_name='captchastore',
            name='added_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
