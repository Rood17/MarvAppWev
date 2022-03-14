from .models import Pagos
import datetime, random

def registrar_pago(pago_dict):
    pago_id = None
    numAle = random.randint(1, 999)
    # save payer
    if pago_dict is not None and len(pago_dict) != 0:
        pago_id = datetime.datetime.today().strftime("%m%d%Y-") + str(pago_dict["idSubscriber"]) + '-' + str(numAle)
        
        if not Pagos.objects.filter(payment_id=pago_id).exists():
            instance = Pagos()
            instance.payment_id = pago_id
            instance.user_number = pago_dict["idSubscriber"]
            instance.paquete = pago_dict["title"]
            instance.cantidad = pago_dict["unit_price"]
            instance.cliente = pago_dict["cliente"]
            instance.email = pago_dict["payer_email"]
            instance.equipo = pago_dict["equipo"]
            instance.payment_status = 'En proceso'
            instance.save()

            print('[INFO] - Pagos : Se realizó registro con éxito.')
    else :
        print('[ERROR] - Pagos : No se ha registrado ningún pago.')
    
    return pago_id

def actualizar_pago(pago_dict):
     # save payer
    if pago_dict is not None and len(pago_dict) != 0:
        instance = Pagos.objects.get(payment_id=pago_dict["payment_id"])
        instance.payment_mercado_id = pago_dict["collection_id"]
        instance.payment_status = pago_dict["payment_status"]
        instance.payment_type = pago_dict["payment_type"]
        instance.merchant_order_id = pago_dict["merchant_order_id"]
        instance.save()

        print('[INFO] - Pagos : Se realizó registro con éxito.')
    else :
        print('[ERROR] - Pagos : No se ha registrado ningún pago.')


