# Generated by Django 2.1.1 on 2020-10-26 07:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0005_auto_20201026_0657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schoolmodel',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='owner.OwnerModel'),
        ),
        migrations.AlterField(
            model_name='schoolmodel',
            name='principal',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='principal.PrincipalModel'),
        ),
    ]
