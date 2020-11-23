# Generated by Django 2.1.1 on 2020-11-10 17:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school_class', '0001_initial'),
        ('subject', '0001_initial'),
        ('teacher', '0003_auto_20201110_1800'),
    ]

    operations = [
        migrations.AddField(
            model_name='teachercontentmodel',
            name='grade',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='school_class.ClassModel'),
        ),
        migrations.AddField(
            model_name='teachercontentmodel',
            name='subject',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='subject.SubjectModel'),
        ),
    ]
