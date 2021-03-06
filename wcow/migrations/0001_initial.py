# Generated by Django 3.0.4 on 2020-04-17 12:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Especie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Predio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ancho', models.DecimalField(decimal_places=3, max_digits=13)),
                ('largo', models.DecimalField(decimal_places=3, max_digits=13)),
            ],
        ),
        migrations.CreateModel(
            name='Plantacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('especie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wcow.Especie')),
            ],
        ),
    ]
