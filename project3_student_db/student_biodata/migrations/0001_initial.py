# Generated by Django 4.2.2 on 2023-08-03 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(default='', max_length=25)),
                ('Age', models.IntegerField(default='')),
                ('Gender', models.CharField(default='', max_length=10)),
                ('Address', models.CharField(default='', max_length=50)),
                ('Email', models.CharField(default='', max_length=15)),
            ],
        ),
    ]
