# Generated by Django 2.0.2 on 2018-02-20 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('bio', models.CharField(max_length=140)),
                ('profile_picture', models.ImageField(upload_to='mainapp/static/mainapp/images/')),
                ('city', models.CharField(max_length=30)),
                ('state', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Volunteer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=30)),
                ('bio', models.CharField(max_length=140)),
                ('profile_picture', models.ImageField(upload_to='mainapp/static/mainapp/images/')),
                ('city', models.CharField(max_length=30)),
                ('state', models.CharField(max_length=2)),
            ],
        ),
    ]
