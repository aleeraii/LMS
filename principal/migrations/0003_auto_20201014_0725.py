# Generated by Django 2.1.1 on 2020-10-14 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0002_auto_20201014_0654'),
    ]

    operations = [
        migrations.AlterField(
            model_name='principalmodel',
            name='pay',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='principalmodel',
            name='qualification',
            field=models.CharField(max_length=500, null=True),
        ),
    ]