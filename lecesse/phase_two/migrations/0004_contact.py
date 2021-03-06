# Generated by Django 2.2 on 2020-02-23 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phase_two', '0003_auto_20200223_0305'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=100)),
                ('position', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=40, unique=True)),
            ],
        ),
    ]
