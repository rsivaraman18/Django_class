# Generated by Django 4.2.2 on 2023-08-14 06:02

from django.db import migrations, models
 
class Migration(migrations.Migration):
 
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate_Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Cname', models.CharField(max_length=100)),
                ('Cgender', models.CharField(max_length=10)),
                ('Cpdf_file', models.FileField(upload_to='pdfs/')),
                ('Cexcel_file', models.FileField(upload_to='excels/')),
                ('Cimage', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
