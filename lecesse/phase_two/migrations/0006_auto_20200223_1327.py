# Generated by Django 2.2 on 2020-02-23 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phase_two', '0005_building'),
    ]

    operations = [
        migrations.AddField(
            model_name='building',
            name='id_project',
            field=models.CharField(default=26, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contact',
            name='id_project',
            field=models.CharField(default='26', max_length=100),
            preserve_default=False,
        ),
    ]