from django.shortcuts import render, get_object_or_404
from .models import CatEventos, CatPaquetes, Categorias, Faqs, Galeria, Paquetes, Portafolio, Servicios, Imagenes

# Create your views here.
def home(request):
    faqs_social = Faqs.objects.filter(clase__id=2)
    faqs_empresarial = Faqs.objects.filter(clase__id=1)
    galeria_social = Galeria.objects.filter(clase__id=2)
    galeria_empresarial = Galeria.objects.filter(clase__id=1)
    paquetes = Paquetes.objects.all()
    portafolio_social = Portafolio.objects.filter(clase__id=2)
    portafolio_empresarial = Portafolio.objects.filter(clase__id=1)
    categorias = Categorias.objects.all().exclude(nombre='Evento')[:5]
    cat_eventos = CatEventos.objects.all()[:5]
    cat_paquete = CatPaquetes.objects.all()[:5]
    imagenes = Imagenes.objects.all()
    img_social = get_object_or_404(Imagenes, name='img_social')
    img_empresarial = get_object_or_404(Imagenes, name='img_empresarial')
    servicios = Servicios.objects.all()
    empresariales = get_object_or_404(Servicios, id=1)
    sociales = get_object_or_404(Servicios, id=2)


    return render(request, 'core/index.html', 
        {
            'img_social' : img_social,
            'img_empresarial' : img_empresarial,
            'empresariales' : empresariales,
            'sociales':sociales,
            'portafolio_social':portafolio_social,
            'portafolio_empresarial':portafolio_empresarial,
            'categorias' :categorias,
            'paquetes' : paquetes,
            'galeria_social':galeria_social,
            'galeria_empresarial':galeria_empresarial,
            'faqs_social':faqs_social,
            'faqs_empresarial':faqs_empresarial,
            'cat_eventos':cat_eventos,
            'cat_paquete':cat_paquete
        })