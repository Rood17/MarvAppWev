from django.contrib import admin
from .models import Galeria, Paquetes, Servicios, Imagenes, Portafolio, Categorias,Faqs, Contacto
# Register your models here.


class ImagenesAdmin (admin.ModelAdmin):
    fieldsets = (
        ('Banner Principal', {
            'fields': ('headImg1', 'headImg2', 'headImg3')
        }),
        ('Eventos Destacados', {
            'fields': ('destacada1', 'titulo_destacada1', 'subHeader_destacada1', 
            'destacada2','titulo_destacada2', 'subHeader_destacada2', 
            'destacada3','titulo_destacada3', 'subHeader_destacada3', 
            'destacada4','titulo_destacada4', 'subHeader_destacada4', 
            'destacada5','titulo_destacada5', 'subHeader_destacada5', ),

        }),
    )
    readonly_fields = ('created', 'updated')
    search_fields = ('titulo', )
    ordering = ('created',)
    date_hierarchy = 'created' 
    
admin.site.register(Imagenes, ImagenesAdmin)

class ServiciosAdmin (admin.ModelAdmin):
    fieldsets = (
        ('Texto Banner Principal', {
            'fields': ('titulo', 'subHeader', 'imagenes')
        }),
    )
    readonly_fields = ('created', 'updated')
    list_display = ('titulo', 'updated')
    search_fields = ('titulo', )
    ordering = ('titulo',)
    date_hierarchy = 'created' 
    
admin.site.register(Servicios, ServiciosAdmin)

class PortafolioAdmin (admin.ModelAdmin):
    fieldsets = (
        ('Elemento', {
            'fields': ('clase',  'categoria','imagen','titulo', 'descripcion')
        }),
    )
    readonly_fields = ('created', 'updated')
    list_display = ('titulo', 'updated')
    search_fields = ('titulo', )
    ordering = ('titulo',)
    date_hierarchy = 'created' 
    
admin.site.register(Portafolio, PortafolioAdmin)

class CategoriasAdmin (admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('nombre', 'updated')
    search_fields = ('nombre', )
    ordering = ('nombre',)
    date_hierarchy = 'created' 
    
admin.site.register(Categorias, CategoriasAdmin)

class PaquetesAdmin (admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('nombre', 'precio')
    search_fields = ('nombre', )
    ordering = ('nombre',)
    date_hierarchy = 'created' 
    
admin.site.register(Paquetes, PaquetesAdmin)

class GaleriaAdmin (admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('titulo',)
    search_fields = ('titulo', )
    ordering = ('titulo',)
    date_hierarchy = 'created' 

admin.site.register(Galeria, GaleriaAdmin)

class FaqsAdmin (admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('pregunta',)
    search_fields = ('pregunta', )
    ordering = ('pregunta',)
    date_hierarchy = 'created' 

admin.site.register(Faqs, FaqsAdmin)

class ContactoAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    date_hierarchy = 'created' 

admin.site.register(Contacto, ContactoAdmin)
