# Generated by Django 2.1.1 on 2020-12-06 18:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('section', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TimeTableModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('assign_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('assign_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='section.SectionModel')),
            ],
        ),
    ]
