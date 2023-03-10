# Generated by Django 4.0.2 on 2023-01-18 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Remera',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=128)),
                ('talle', models.IntegerField(choices=[('1', 'XS'), ('2', 'S'), ('3', 'M'), ('4', 'L'), ('5', 'XL'), ('6', 'XXL')])),
                ('color', models.CharField(max_length=128)),
                ('lisa', models.BooleanField()),
                ('genero', models.IntegerField(choices=[('1', 'Hombre'), ('2', 'Mujer'), ('3', 'Unisex')])),
            ],
        ),
    ]
