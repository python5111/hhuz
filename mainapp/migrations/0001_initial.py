# Generated by Django 4.0.3 on 2022-06-03 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job_creat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(max_length=35)),
                ('citiy', models.CharField(choices=[('Toshkent', 'Toshkent'), ('Buxoro', 'Buxoro'), ("Farg'ona", "Farg'ona"), ('Samarqand', 'Samarqand'), ('Andijon', 'Andijon'), ('Surxondaryo', 'Surxondaryo')], default='Toshkent', max_length=11)),
                ('salary_min', models.PositiveIntegerField(blank=True, null=True)),
                ('salary_max', models.PositiveIntegerField(blank=True, null=True)),
                ('age', models.CharField(max_length=25, null=True)),
                ('experience', models.CharField(max_length=155, null=True)),
                ('phone', models.CharField(max_length=13)),
                ('decription', models.TextField()),
                ('register_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('active', 'active'), ('passive', 'passive')], default='active', max_length=8)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='media/')),
            ],
        ),
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=85)),
                ('genders', models.CharField(choices=[('Erkak', 'Erkak'), ('Ayol', 'Ayol')], default='Erkak', max_length=5)),
                ('citiy', models.CharField(choices=[('Toshkent', 'Toshkent'), ('Buxoro', 'Buxoro'), ("Farg'ona", "Farg'ona"), ('Samarqand', 'Samarqand'), ('Andijon', 'Andijon'), ('Surxondaryo', 'Surxondaryo')], default='Toshkent', max_length=11)),
                ('phone', models.CharField(max_length=13)),
                ('birth_date', models.DateField(null=True)),
                ('register_date', models.DateTimeField(auto_now_add=True)),
                ('experience', models.PositiveIntegerField(null=True)),
                ('salary', models.PositiveIntegerField(null=True)),
                ('decription', models.TextField()),
            ],
        ),
    ]
