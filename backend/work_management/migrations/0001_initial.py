# Generated by Django 2.1.5 on 2019-01-31 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WorkProgrammedORM',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('creationDate', models.DateTimeField(auto_now_add=True)),
                ('ownerOfNet', models.CharField(blank=True, max_length=500)),
                ('description', models.CharField(blank=True, max_length=500)),
                ('actualStartTime', models.DateTimeField(auto_now_add=True)),
                ('actualEndTime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]