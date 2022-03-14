from django.urls import path, include
from .views import get_preferences, payment_success, payment_failure, payment_pending


urlpatterns = [
    
# Index admin
   path('generar_pago', get_preferences, name="payment"),
   path('payment_success/<str:payment_id>', payment_success, name = 'payment_success'),
   path('payment_failure/<str:payment_id>', payment_failure, name = 'payment_failure'),
   path('payment_pending/<str:payment_id>', payment_pending, name = 'payment_pending'),
]