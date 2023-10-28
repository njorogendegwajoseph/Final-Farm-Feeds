from django.urls import path
from . import views
from .views import C2BPaymentView

app_name = 'payment'

urlpatterns = [
    path('process/', views.payment_process, name='process'),
    path('done/', views.payment_done, name='done'),
    path('cancelled/', views.payment_canceled, name='cancelled'),
    path('c2b-payment/', C2BPaymentView.as_view(), name='c2b_payment'),
]