from .models import Contacto
import json

def ctx_dict(request):
    ctx = {}
    links = Contacto.objects.all()
    for link in links:
        ctx[link.key] = link.url
    return ctx
