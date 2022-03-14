from django.db import models
from ckeditor.fields import RichTextField

class CatPaquetes(models.Model):
    nombre = models.CharField(max_length=200, verbose_name="Título")

    created = models.DateTimeField(
        verbose_name="Fecha de creación", auto_now_add=True)
    updated = models.DateTimeField(
        verbose_name="Fecha de edición", auto_now=True)
    class Meta:
        verbose_name = 'Tipo de Eventos'
        verbose_name_plural = 'Tipo de Eventos'
        # Ordenar de más nuevos a más viejos
        ordering= ['-created']
        
    def __str__(self):
        return self.nombre

class CatEventos(models.Model):
    nombre = models.CharField(max_length=200, verbose_name="Título")

    created = models.DateTimeField(
        verbose_name="Fecha de creación", auto_now_add=True)
    updated = models.DateTimeField(
        verbose_name="Fecha de edición", auto_now=True)
    class Meta:
        verbose_name = 'Tipo de Eventos'
        verbose_name_plural = 'Tipo de Eventos'
        # Ordenar de más nuevos a más viejos
        ordering= ['-created']
        
    def __str__(self):
        return self.nombre

class Categorias(models.Model):
    nombre = models.CharField(max_length=200, verbose_name="Título")

    created = models.DateTimeField(
        verbose_name="Fecha de creación", auto_now_add=True)
    updated = models.DateTimeField(
        verbose_name="Fecha de edición", auto_now=True)
    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
        # Ordenar de más nuevos a más viejos
        ordering= ['-created']
        
    def __str__(self):
        return self.nombre


# Create your models here.
class Imagenes(models.Model):

    name = models.CharField(
        max_length=200, 
    verbose_name="Título",
    default="Nombre grupo del grupo de imgs",
    help_text="tip: Poner nombre relacionado al servico. Ej... 'Imgs_Social'."
    )

    # Header
    headImg1 = models.ImageField(
        upload_to ='marvImgs/uploads/', 
        verbose_name="Imagen Banner 1")
    headImg2 = models.ImageField(
        upload_to ='marvImgs/uploads/', 
        verbose_name="Imagen Banner 2")
    headImg3 = models.ImageField(
        upload_to ='marvImgs/uploads/', 
        verbose_name="Imagen Banner 3")

    # Destacadas
    destacada1 = models.ImageField(
        upload_to ='eventos/destacados/', 
        verbose_name="Evento destacado 1")
    titulo_destacada1 = models.CharField(max_length=200, 
    verbose_name="Título", 
    help_text="Título para Imagen destacada")
    subHeader_destacada1 = models.TextField(max_length=200, 
    verbose_name="Texto descriptivo Header", 
    help_text="Breve descripción, max. 200 caracteres." 
    )
    
    destacada2 = models.ImageField(
        upload_to ='marvImgs/eventos/destacados/', 
        verbose_name="Evento destacado 2")
    titulo_destacada2 = models.CharField(max_length=200, 
    verbose_name="Título", 
    help_text="Título para Imagen destacada")
    subHeader_destacada2 = models.TextField(max_length=200, 
    verbose_name="Texto descriptivo Header", 
    help_text="Breve descripción, max. 200 caracteres." 
    )
    
    destacada3 = models.ImageField(
        upload_to ='marvImgs/eventos/destacados/', 
        verbose_name="Evento destacado 3")
    titulo_destacada3 = models.CharField(max_length=200, 
    verbose_name="Título", 
    help_text="Título para Imagen destacada")
    subHeader_destacada3 = models.TextField(max_length=200, 
    verbose_name="Texto descriptivo Header", 
    help_text="Breve descripción, max. 200 caracteres." 
    )
    
    destacada4 = models.ImageField(
        upload_to ='marvImgs/eventos/destacados/', 
        verbose_name="Evento destacado 4")
    titulo_destacada4 = models.CharField(max_length=200, 
    verbose_name="Título", 
    help_text="Título para Imagen destacada")
    subHeader_destacada4 = models.TextField(max_length=200, 
    verbose_name="Texto descriptivo Header", 
    help_text="Breve descripción, max. 200 caracteres." 
    )
    
    
    destacada5 = models.ImageField(
        upload_to ='marvImgs/eventos/destacados/', 
        verbose_name="Evento destacado 5")
    titulo_destacada5 = models.CharField(max_length=200, 
    verbose_name="Título", 
    help_text="Título para Imagen destacada")
    subHeader_destacada5 = models.TextField(max_length=200, 
    verbose_name="Texto descriptivo Header", 
    help_text="Breve descripción, max. 200 caracteres." 
    )
    

    created = models.DateTimeField(
        verbose_name="Fecha de creación", auto_now_add=True)
    updated = models.DateTimeField(
        verbose_name="Fecha de edición", auto_now=True)
    class Meta:
        verbose_name = 'Imágenes'
        verbose_name_plural = 'Imágenes'
        # Ordenar de más nuevos a más viejos
        ordering= ['-created']
        
    def __str__(self):
        return self.name

# Create your models here.
class Servicios(models.Model):
    id = models.AutoField(                     
                            primary_key=True,
                        )
    titulo = models.CharField(max_length=200, verbose_name="Título")
    subHeader = models.TextField(max_length=200, verbose_name="Texto descriptivo Header" )
    
    imagenes = models.ForeignKey(Imagenes, on_delete=models.PROTECT,
                    blank=True, null=True,
                    verbose_name='Imágenes',
                    related_name="img_service"
               )
    
    created = models.DateTimeField(
        verbose_name="Fecha de creación", auto_now_add=True)
    updated = models.DateTimeField(
        verbose_name="Fecha de edición", auto_now=True)
    class Meta:
        verbose_name = 'Servicio'
        verbose_name_plural = 'Servicios'
        # Ordenar de más nuevos a más viejos
        ordering= ['-created']
        
    def __str__(self):
        return self.titulo

class Portafolio(models.Model):
    clase = models.ManyToManyField(
        Servicios, 
        verbose_name='Servicio relacionado', 
        help_text="Seleccione una o las dos clases de servicio.")
    TYPE_LIST = (
            ('E', 'Equipo'),
            ('v', 'Evento'),
    )
    tipo = models.CharField(max_length=1, choices=TYPE_LIST, verbose_name="Tipo", default="E")
    categoria = models.ManyToManyField(
        Categorias,
        verbose_name="Categorías",
        help_text="Seleccione una o varias categorías relacionadas al item.",
        null=True, blank=True)
    cat_eventos = models.ManyToManyField(
        CatEventos,
        verbose_name="Eventos",
        help_text="Seleccione una o varios eventos relacionadas al item.",
        null=True, blank=True)
    imagen = models.ImageField(
        upload_to ='marvImgs/portafolio/', 
        verbose_name="Imagen")
    titulo = models.CharField(max_length=200, verbose_name="Título")
    descripcion = models.TextField(max_length=200, verbose_name="Breve descripción" )

    created = models.DateTimeField(
        verbose_name="Fecha de creación", auto_now_add=True)
    updated = models.DateTimeField(
        verbose_name="Fecha de edición", auto_now=True)

    class Meta:
        verbose_name = 'Portafolio'
        verbose_name_plural = 'Portafolio'
        # Ordenar de más nuevos a más viejos
        ordering= ['-created']
        
    def __str__(self):
        return self.titulo

class Paquetes(models.Model):
    nombre = models.CharField(max_length=200, verbose_name="Nombre")
    precio = models.CharField(max_length=200, verbose_name="Precio")
    cat_paquete = models.ManyToManyField(
        CatPaquetes,
        verbose_name="Categorías",
        help_text="Seleccione una o varias categorías relacionadas al item.",
        null=True, blank=True)
    cat_eventos = models.ManyToManyField(
        CatEventos,
        verbose_name="Eventos",
        help_text="Seleccione una o varios eventos relacionadas al item.",
        null=True, blank=True)
    descripcion = models.TextField(max_length=200, verbose_name="Breve descripción")
    caracteristicas = models.TextField(max_length=600, verbose_name="Características")
    created = models.DateTimeField(
        verbose_name="Fecha de creación", auto_now_add=True)
    updated = models.DateTimeField(
        verbose_name="Fecha de edición", auto_now=True)
    class Meta:
        verbose_name = 'Paquete'
        verbose_name_plural = 'Paquetes'
        # Ordenar de más nuevos a más viejos
        ordering= ['-created']
        
    def __str__(self):
        return self.nombre

class Galeria(models.Model):
    id = models.AutoField(                     
                            primary_key=True,
                        )
    clase = models.ManyToManyField(
        Servicios, 
        verbose_name='Servicio relacionado', 
        help_text="Seleccione una o las dos clases de servicio.")
    titulo = models.CharField(max_length=200, verbose_name="Título",
    blank = True,null=True)
    descripcion = models.TextField(max_length=200, verbose_name="Breve descripción",
    blank = True,null=True)
    imagen = models.ImageField(
        upload_to ='marvImgs/galeria/', 
        verbose_name="Imagen Banner 1")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = 'Galería'
        verbose_name_plural = 'Galería'
        # Ordenar de más nuevos a más viejos
        ordering= ['-created']
        
    def __str__(self):
        return str(self.id)

class Faqs(models.Model):
    clase = models.ManyToManyField(
        Servicios, 
        verbose_name='Servicio relacionado', 
        help_text="Seleccione una o las dos clases de servicio.")
    pregunta = models.CharField(max_length=200, verbose_name="Pregunta")
    respuesta = models.TextField(max_length=200, verbose_name=" Respuesta")

    created = models.DateTimeField(
        verbose_name="Fecha de creación", auto_now_add=True)
    updated = models.DateTimeField(
        verbose_name="Fecha de edición", auto_now=True)
    class Meta:
        verbose_name = 'Faq'
        verbose_name_plural = 'Faqs'
        # Ordenar de más nuevos a más viejos
        ordering= ['-created']
        
    def __str__(self):
        return self.pregunta  

class Contacto(models.Model):
    key = models.SlugField( 
        verbose_name="Nombre clave", max_length=100, unique=True)
    name = models.CharField( 
        verbose_name="Red social o Número", max_length=200)
    url = models.URLField(
        verbose_name="Enlace", max_length=200, null=True, blank=True)
    created = models.DateTimeField(
        verbose_name="Fecha de creación", auto_now_add=True)
    updated = models.DateTimeField(
        verbose_name="Fecha de edición", auto_now=True)

    class Meta:
        verbose_name = "enlace"
        verbose_name_plural = "enlaces"
        ordering = ['name']

    def __str__(self):
        return self.name