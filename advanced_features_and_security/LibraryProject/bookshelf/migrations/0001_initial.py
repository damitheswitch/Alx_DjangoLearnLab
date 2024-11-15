# Generated by Django 5.1.2 on 2024-11-02 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name= 'CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_birth', models.DateField(null=True, blank=True)),
                ('profile_photo', models.ImageField(upload_to='profile_photos/', null=True, blank=True)),
            ],
        ),
    ]