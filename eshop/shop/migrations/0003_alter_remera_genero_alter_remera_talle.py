# Generated by Django 4.0.2 on 2023-01-23 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_alter_remera_genero_alter_remera_talle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='remera',
            name='genero',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Hombre'), (2, 'Mujer'), (3, 'Unisex')], null=True),
        ),
        migrations.AlterField(
            model_name='remera',
            name='talle',
            field=models.PositiveSmallIntegerField(choices=[(1, 'XS'), (2, 'S'), (3, 'M'), (4, 'L'), (5, 'XL'), (6, 'XXL')], null=True),
        ),
    ]