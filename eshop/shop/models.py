from django.db import models

# Create your models here.

class Remera(models.Model):
    TALLES = (
        (1,'XS'),
        (2,'S'),
        (3, 'M'),
        (4, 'L'),
        (5, 'XL'),
        (6, 'XXL')
    )

    GENEROS = (
        (1, 'Hombre'),
        (2, 'Mujer'),
        (3, 'Unisex')
    )
    marca = models.CharField('Marca',max_length=128)
    talle = models.PositiveSmallIntegerField('Talle', choices=TALLES, null=True)
    color = models.CharField('Color',max_length=128)
    lisa = models.BooleanField('Lisa')
    genero = models.PositiveSmallIntegerField('Genero',choices=GENEROS, null=True)

    def __str__(self):
        return f'{self.marca} {self.color} {self.get_talle_display()}'
