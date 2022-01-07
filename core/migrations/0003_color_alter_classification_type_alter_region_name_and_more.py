# Generated by Django 4.0.1 on 2022-01-07 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_region_name_classification'),
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name='classification',
            name='type',
            field=models.CharField(choices=[('AOC', 'AOC'), ('AOP', 'AOP'), ('IGP', 'IGP'), ('VDP', 'Vin de Pays'), ('Autre', 'Autre')], default='AOC', max_length=10),
        ),
        migrations.AlterField(
            model_name='region',
            name='name',
            field=models.CharField(max_length=150, unique=True),
        ),
        migrations.AddConstraint(
            model_name='classification',
            constraint=models.UniqueConstraint(fields=('type', 'name'), name='unique_type_name'),
        ),
    ]
