# Generated by Django 3.1.5 on 2021-04-23 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Matche',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mdate', models.DateField()),
                ('mmatch', models.CharField(max_length=64)),
                ('mtime', models.TimeField()),
                ('mvenue', models.CharField(max_length=64)),
                ('mmypred', models.CharField(max_length=64)),
            ],
        ),
    ]
