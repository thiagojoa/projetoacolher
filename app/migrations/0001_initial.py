# Generated by Django 2.1.2 on 2018-10-31 01:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CargoDirigente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cargo', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Dirigente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('cpf', models.CharField(max_length=10)),
                ('cargo', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app.CargoDirigente')),
            ],
        ),
    ]
