# Generated by Django 2.2 on 2020-02-23 14:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('phase_one', '0006_provider_material'),
        ('phase_two', '0006_auto_20200223_1327'),
    ]

    operations = [
        migrations.CreateModel(
            name='various',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_measure', models.CharField(choices=[('FEET', 'FEET'), ('INCHES', 'INCHES')], max_length=100, null=True)),
                ('area', models.CharField(max_length=150, null=True)),
                ('price', models.ImageField(upload_to='model_apto')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('provider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='phase_one.Provider')),
            ],
        ),
    ]