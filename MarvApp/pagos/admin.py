from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# Register your models here.
from .models import Pagos

class PagosAdmin(admin.ModelAdmin):
    date_hierarchy = 'created'
    list_display = (
        'nombre','payment_status', 'paquete', 'cantidad' 
        )
    list_filter = ( 'payment_type',)
    fieldsets = (
        ('Datos cliente', {
            'fields': ('nombre','user_number','email')
        }),
        ('', {
            'fields': ('paquete', 'cantidad')
        }),
        ('Datos Mercado Pago', {
            'fields': ('payment_mercado_id', 'payment_status', 'payment_type', 'merchant_order_id')
        }),
        
    )
    readonly_fields = ('created', 'updated')

admin.site.register(Pagos, PagosAdmin)

