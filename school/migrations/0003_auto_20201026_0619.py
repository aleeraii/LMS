# Generated by Django 2.1.1 on 2020-10-26 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0002_auto_20201015_0659'),
    ]

    operations = [
        migrations.CreateModel(
            name='FunctionalityModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=300)),
            ],
        ),
        migrations.AddField(
            model_name='schoolmodel',
            name='student_functionality',
            field=models.ManyToManyField(to='school.FunctionalityModel'),
        ),
    ]