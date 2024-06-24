# Generated by Django 5.0.6 on 2024-06-22 19:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_alter_student_section'),
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='section_teacher',
            name='teacher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.teacher'),
        ),
    ]
