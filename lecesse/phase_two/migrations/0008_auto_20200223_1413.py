# Generated by Django 2.2 on 2020-02-23 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phase_two', '0007_various'),
    ]

    operations = [
        migrations.AlterField(
            model_name='various',
            name='price',
            field=models.CharField(max_length=150, null=True),
        ),
    ]