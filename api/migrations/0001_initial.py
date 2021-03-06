# Generated by Django 3.2.5 on 2021-07-06 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=64)),
                ('lastname', models.CharField(max_length=64)),
                ('barber', models.CharField(blank=True, max_length=64, null=True)),
                ('phone', models.CharField(max_length=12)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('contact', models.CharField(blank=True, max_length=64, null=True)),
                ('date', models.DateField()),
                ('time', models.CharField(max_length=64)),
                ('comment', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
