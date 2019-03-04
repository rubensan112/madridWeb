# Generated by Django 2.1.7 on 2019-02-25 22:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AffectedEntityORM',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('provider', models.CharField(max_length=100)),
                ('reference_number', models.CharField(max_length=300)),
                ('reference_type', models.CharField(choices=[('type1', 'Freshman'), ('type2', 'Sophomore'), ('type3', 'Junior'), ('type4', 'Senior')], max_length=100)),
                ('administrative_number', models.CharField(max_length=300)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ChangeRequestORM',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField(null=True, verbose_name='Date and time when the change implementation is started')),
                ('end_date', models.DateTimeField(null=True, verbose_name='Date and time when the change implementation is finished')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EmailORM',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender', models.CharField(max_length=100)),
                ('receiver', models.CharField(max_length=100)),
                ('subject', models.TextField(max_length=1000)),
                ('body', models.TextField(max_length=5000)),
                ('received_date', models.DateTimeField(verbose_name='Date and time when the email was received')),
                ('change_request', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='email', to='change_management.ChangeRequestORM')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RemedyStateORM',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.IntegerField(choices=[(0, 'CRQ created'), (1, 'CRQ in progress'), (2, 'CRQ closed')])),
                ('url', models.URLField()),
                ('id_ticket', models.CharField(max_length=100)),
                ('creator_name', models.CharField(max_length=100)),
                ('creator_departament', models.CharField(max_length=100)),
                ('change_request', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='remedy_state', to='change_management.ChangeRequestORM')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='affectedentityorm',
            name='change_request',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='affected_entity', to='change_management.ChangeRequestORM'),
        ),
    ]