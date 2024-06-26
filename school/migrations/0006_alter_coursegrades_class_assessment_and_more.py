# Generated by Django 5.0.6 on 2024-06-23 09:06

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0005_alter_section_teacher_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursegrades',
            name='class_assessment',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(20)]),
        ),
        migrations.AlterField(
            model_name='coursegrades',
            name='final_exam_result',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(50)]),
        ),
        migrations.AlterField(
            model_name='coursegrades',
            name='grade',
            field=models.CharField(max_length=2),
        ),
        migrations.AlterField(
            model_name='coursegrades',
            name='mid_exam_result',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(30)]),
        ),
    ]
