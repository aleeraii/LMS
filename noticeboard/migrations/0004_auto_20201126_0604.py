# Generated by Django 2.1.1 on 2020-11-26 06:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('noticeboard', '0003_auto_20201125_0529'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='noticeboardmodel',
            options={'ordering': ['date']},
        ),
    ]
