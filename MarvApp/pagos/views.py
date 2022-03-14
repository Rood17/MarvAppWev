from django.shortcuts import render
import mercadopago
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect
import datetime, random
from .utils import actualizar_pago
from rest_framework.decorators import api_view
from rest_framework.response import Response




# Create your views here.
#globals
# For app mobile production
def get_preferences(request):

    preference = None
    cliente=None
    print('***************************** : ' + request.method)
    if request.method == 'POST' and request.POST.get('name'):
        # contact_form = RegisterForms(data=request.POST)
        userDataDict = dict(request.POST)
        name = request.POST.get('name')
        print('***************************** name : ' + name)


        sdk = mercadopago.SDK(
            "TEST-841140758152091-022419-91c57d2db15afa4c2e9135d80129bd1e-1074815822")

        print(' Calling for preference link')
        # Necesita recibir el producto y el precio
        # datos del usuario
        # registrarlo en la bd
        idSubscriber = 8888888888
        title = request.POST.get('producto')
        unit_price = int(request.POST.get('precio'))
        payer_email =request.POST.get('email')
        first_name=request.POST.get('name')
        last_name=request.POST.get('lastName')
        cliente = first_name + ' ' + last_name

        print("unit_price : " , type(unit_price))
        # brand = get_device_brand(idSubscriber)  
        brand = ' - '
        # Set pago dict
        pago_id = cliente + str(random.randint(0, 999999))

        urlSuccess = "https://jrmovil.pythonanywhere.com/jr_api/cm/1.0/payment_success/" + pago_id
        urlFailure = "https://jrmovil.pythonanywhere.com/jr_api/cm/1.0/payment_failure/" + pago_id
        urlPending = "https://jrmovil.pythonanywhere.com/jr_api/cm/1.0/payment_pending/" + pago_id

        preference_data = {
            "items": [
                {
                    "title": title,
                    "quantity": 1,
                    "unit_price": unit_price,
                }
            ],
            "payer": {
                "name": first_name,
                "surname": last_name,
                "email": payer_email,
                "phone": {
                    "area_code": "51",
                    "number": idSubscriber
                },
                "identification": {
                    "type": "DNI",
                    "number": "none"
                },

            },
            "back_urls" : {
                    "success": urlSuccess,
                    "failure": urlFailure,
                },
            "auto_return": "approved",
            "additional_info": "JMarvEventos",
        }

        preference_response = sdk.preference().create(preference_data)
        preference = preference_response["response"]
    
    print(' **** ** : ', preference)
    return render(request, 'pagos/mercado_pro.html', {
        'preference': preference, 'cliente' : cliente})


@api_view(['GET'])
def payment_success(request, payment_id):
    # busque el tipo de celular
    # registrar pago
    collection_id = request.GET.get('collection_id')
    payment_status = request.GET.get('collection_status')
    payment_type = request.GET.get('payment_type')
    merchant_order_id = request.GET.get('merchant_order_id')


    pago_dict = {
        'payment_id' : payment_id,
        'collection_id' : collection_id,
        'payment_status' : payment_status,
        'payment_type' : payment_type,
        'merchant_order_id' : merchant_order_id
    }
    print(" ************************ : 1 ", payment_status)
    actualizar_pago(pago_dict)
    return Response(True)

@api_view(['GET'])
def payment_failure(request, payment_id):
    # busque el tipo de celular
    # registrar pago
    collection_id = request.GET.get('collection_id')
    payment_status = request.GET.get('collection_status')
    payment_type = request.GET.get('payment_type')
    merchant_order_id = request.GET.get('merchant_order_id')


    pago_dict = {
        'payment_id' : payment_id,
        'collection_id' : collection_id,
        'payment_status' : payment_status,
        'payment_type' : payment_type,
        'merchant_order_id' : merchant_order_id
    }
    print(" ************************ :   2 ", payment_status)
    actualizar_pago(pago_dict)
    return Response(True)

@api_view(['GET'])
def payment_pending(request, payment_id):
    # busque el tipo de celular
    # registrar pago
    collection_id = request.GET.get('collection_id')
    payment_status = request.GET.get('collection_status')
    payment_type = request.GET.get('payment_type')
    merchant_order_id = request.GET.get('merchant_order_id')


    pago_dict = {
        'payment_id' : payment_id,
        'collection_id' : collection_id,
        'payment_status' : payment_status,
        'payment_type' : payment_type,
        'merchant_order_id' : merchant_order_id
    }
    print(" ************************ :  3 ", payment_status)
    actualizar_pago(pago_dict)
    
    return Response(True)
