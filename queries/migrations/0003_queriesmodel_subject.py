# Generated by Django 2.1.1 on 2020-12-07 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('queries', '0002_queriesmodel_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='queriesmodel',
            name='subject',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
