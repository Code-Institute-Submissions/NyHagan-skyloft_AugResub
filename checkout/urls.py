from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views
from .webhooks import webhook

urlpatterns = [
    path('', login_required(views.checkout), name='checkout'),
    path('checkout_success/<order_number>',
         views.checkout_success, name='checkout_success'),
    path('cache_checkout_data/', views.cache_checkout_data,
         name='cache_checkout_data'),
    path('wh/', webhook, name='webhook'),
]
