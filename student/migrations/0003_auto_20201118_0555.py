# Generated by Django 2.1.1 on 2020-11-18 05:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_studentmodel_school'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentmodel',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='parent.ParentModel'),
        ),
    ]