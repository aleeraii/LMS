# Generated by Django 2.1.1 on 2020-10-26 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0006_auto_20201026_0711'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='FunctionalityModel',
            new_name='FunctionModel',
        ),
        migrations.RemoveField(
            model_name='schoolmodel',
            name='student_functionality',
        ),
        migrations.AddField(
            model_name='schoolmodel',
            name='admin_function',
            field=models.ManyToManyField(related_name='_schoolmodel_admin_function_+', to='school.FunctionModel'),
        ),
        migrations.AddField(
            model_name='schoolmodel',
            name='owner_function',
            field=models.ManyToManyField(related_name='_schoolmodel_owner_function_+', to='school.FunctionModel'),
        ),
        migrations.AddField(
            model_name='schoolmodel',
            name='parent_function',
            field=models.ManyToManyField(related_name='_schoolmodel_parent_function_+', to='school.FunctionModel'),
        ),
        migrations.AddField(
            model_name='schoolmodel',
            name='principal_function',
            field=models.ManyToManyField(related_name='_schoolmodel_principal_function_+', to='school.FunctionModel'),
        ),
        migrations.AddField(
            model_name='schoolmodel',
            name='student_function',
            field=models.ManyToManyField(related_name='_schoolmodel_student_function_+', to='school.FunctionModel'),
        ),
        migrations.AddField(
            model_name='schoolmodel',
            name='teacher_function',
            field=models.ManyToManyField(related_name='_schoolmodel_teacher_function_+', to='school.FunctionModel'),
        ),
    ]