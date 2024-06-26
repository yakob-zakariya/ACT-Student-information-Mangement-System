# Generated by Django 5.0.6 on 2024-06-17 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_delete_departmenthead_delete_registrar_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='DepartmentHead',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=True)),
                ('profile_image', models.ImageField(blank=True, default='profile_image/default.jpg', null=True, upload_to='profile_image')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=True)),
                ('profile_image', models.ImageField(blank=True, default='profile_image/default.jpg', null=True, upload_to='profile_image')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=True)),
                ('profile_image', models.ImageField(blank=True, default='profile_image/default.jpg', null=True, upload_to='profile_image')),
            ],
        ),
    ]
