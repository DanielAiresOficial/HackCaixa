from django.db import models

class Produto(models.Model):
    CO_PRODUTO = models.IntegerField(primary_key=True)
    NO_PRODUTO = models.CharField(max_length=200)
    PC_TAXA_JUROS = models.DecimalField(max_digits=10, decimal_places=9)
    NU_MINIMO_MESES = models.SmallIntegerField()
    NU_MAXIMO_MESES = models.SmallIntegerField(null=True)
    VR_MINIMO = models.DecimalField(max_digits=18, decimal_places=2)
    VR_MAXIMO = models.DecimalField(max_digits=18, decimal_places=2, null=True)

"""
 from .models import Produto

produto1 = Produto(CO_PRODUTO=1, NO_PRODUTO='Produto 1', PC_TAXA_JUROS=0.017900000, NU_MINIMO_MESES=0, NU_MAXIMO_MESES=24, VR_MINIMO=200.00, VR_MAXIMO=10000.00)
produto1.save()

produto2 = Produto(CO_PRODUTO=2, NO_PRODUTO='Produto 2', PC_TAXA_JUROS=0.017500000, NU_MINIMO_MESES=25, NU_MAXIMO_MESES=48, VR_MINIMO=10001.00, VR_MAXIMO=100000.00)
produto2.save()

produto3 = Produto(CO_PRODUTO=3, NO_PRODUTO='Produto 3', PC_TAXA_JUROS=0.018200000, NU_MINIMO_MESES=49, NU_MAXIMO_MESES=96, VR_MINIMO=100000.01, VR_MAXIMO=1000000.00)
produto3.save()

produto4 = Produto(CO_PRODUTO=4, NO_PRODUTO='Produto 4', PC_TAXA_JUROS=0.015100000, NU_MINIMO_MESES=96, NU_MAXIMO_MESES=None, VR_MINIMO=1000000.01, VR_MAXIMO=None)
produto4.save()

"""

