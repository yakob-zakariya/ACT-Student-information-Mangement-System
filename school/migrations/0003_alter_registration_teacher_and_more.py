# Generated by Django 5.0.6 on 2024-06-22 20:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_alter_student_section'),
        ('school', '0002_alter_section_teacher_teacher'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='teacher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='course_teach', to='accounts.teacheruser'),
        ),
        migrations.AlterField(
            model_name='section_teacher',
            name='teacher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.teacheruser'),
        ),
    ]