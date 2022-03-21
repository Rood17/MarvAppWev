from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Pagos(models.Model):
    nombre = models.CharField(
        verbose_name="Nombre del cliente", 
        max_length=60,
        blank=True,null=True)
    user_number = models.CharField(
        verbose_name="Número", 
        max_length=10,
        blank=True,null=True)
    email = models.EmailField(verbose_name='Email', blank=True, null=True, )
    paquete = models.CharField(
        verbose_name="Nombre de la compra", 
        max_length=60)
    cantidad = models.IntegerField(verbose_name='Valor')
    # Foreign key nulleable
    payment_mercado_id =  models.CharField(
        verbose_name="Id del movimeinto en mercado pago", 
        max_length=20, null=True, blank=True)
    payment_status =  models.CharField(
        verbose_name="Status del pago", 
        max_length=20, null=True, blank=True)
    payment_type =  models.CharField(
        verbose_name="Tipo de pago", 
        max_length=18, null=True, blank=True)
    merchant_order_id =  models.CharField(
        verbose_name="merchant_order_id", 
        max_length=20, null=True, blank=True)
    

    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        verbose_name = 'Pagos'
        verbose_name_plural = 'Pagos'
        # Ordenar de más nuevos a más viejos
        
    def __str__(self):
        return self.user_number