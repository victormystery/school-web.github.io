# Generated by Django 4.0.4 on 2022-04-17 22:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Child',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(max_length=50)),
                ('other', models.CharField(max_length=150)),
                ('DOB', models.DateField()),
                ('LGA', models.CharField(max_length=150)),
                ('State', models.CharField(max_length=150)),
                ('Home_address', models.TextField()),
                ('Previous_school', models.TextField()),
                ('Previous_class', models.CharField(max_length=50)),
                ('from_duration', models.DateField()),
                ('to_duration', models.DateField()),
                ('Sex', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='register.gender')),
            ],
        ),
    ]
