# Generated by Django 2.1.1 on 2020-11-24 07:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timetablemodel',
            name='assign_to',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='section.SectionModel'),
        ),
    ]
