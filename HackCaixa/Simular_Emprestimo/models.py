from django.db import models

class Produto(models.Model):
    CO_PRODUTO = models.IntegerField(primary_key=True)
    NO_PRODUTO = models.CharField(max_length=200)
    PC_TAXA_JUROS = models.DecimalField(max_digits=10, decimal_places=9)
    NU_MINIMO_MESES = models.SmallIntegerField()
    NU_MAXIMO_MESES = models.SmallIntegerField(null=True)
    VR_MINIMO = models.DecimalField(max_digits=18, decimal_places=2)
    VR_MAXIMO = models.DecimalField(max_digits=18, decimal_places=2, null=True)
