# Generated by Django 2.1.1 on 2020-12-08 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('queries', '0004_queriesmodel_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='queriesmodel',
            name='query_status',
            field=models.BooleanField(default=1),
        ),
    ]
