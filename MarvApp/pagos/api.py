from .utils import actualizar_pago
from rest_framework.response import Response
import mercadopago
from rest_framework.decorators import api_view

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