# Generated by Django 2.2 on 2020-02-20 04:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phase_one', '0002_auto_20200220_0342'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='material',
            name='icon',
        ),
    ]