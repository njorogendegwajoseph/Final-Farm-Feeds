import braintree
from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from orders.models import Order
from django.contrib import messages
# instantiate Braintree payment gateway
gateway = braintree.BraintreeGateway(settings.BRAINTREE_CONF)

def payment_process(request):
    order_id = request.session.get('order_id')
    order = get_object_or_404(Order, id=order_id)
    total_cost = order.get_total_cost()
    

    if request.method == 'POST':
        nonce = request.POST.get('payment_method_nonce', None)   

        try:
            # Create and submit transaction
            result = gateway.transaction.sale({
                'amount': f'{total_cost:.2f}',
                'payment_method_nonce': nonce,
                'options': {
                    'submit_for_settlement': True
                }
            })

            if result.is_success:
                order.paid = True
                order.braintree_id = result.transaction.id
                order.save()
                return redirect('payment:done')
            else:
                messages.error(request, f"Transaction failed: {result.message}")
                return redirect('payment:cancelled')

        except Exception as e:
            messages.error(request, f"An error occurred: {str(e)}")
            return redirect('payment:cancelled')

    else:
        try:
            client_token = gateway.client_token.generate()
        except Exception as e:
            messages.error(request, f"An error occurred while generating client token: {str(e)}")
            return redirect('payment:cancelled')

        return render(request, 'payment/process.html', {'order': order, 'client_token': client_token})
    
def payment_done(request):
    return render(request, 'payment/done.html')

def payment_canceled(request):
    return render(request, 'payment/cancelled.html')


# Safcom
import requests
from django.http import JsonResponse
from django.views import View

class C2BPaymentView(View):
    def get(self, request):
        # The URL where Daraja API will send the response after the payment is completed
        callback_url = '{% url "payment:payment_done" %}'

        # Replace with your own Daraja API sandbox credentials
        consumer_key = 'KbYuXdIkGbQGRyaD154TSAMkTwKoZr6k'
        consumer_secret = 'quKoCnVYLG5vwbSZ'

        # Sample request payload for initiating a C2B payment
        payload = {
            'ShortCode': 'YOUR_SHORTCODE',
            'CommandID': 'CustomerPayBillOnline',
            'Amount': '1',  # Amount to be paid by the customer
            'Msisdn': '25471750070',  # Customer's phone number
            'BillRefNumber': '12345678',  # Unique bill reference number
            'CallBackURL': callback_url,
            'AccountReference': 'YourAppReference',
        }

        api_url = 'https://sandbox.safaricom.co.ke/mpesa/c2b/v1/simulate'

        headers = {
            'Authorization': 'Bearer YOUR_ACCESS_TOKEN',
            'Content-Type': 'application/json',
        }

        response = requests.post(api_url, json=payload, headers=headers)
        

        return redirect('payment:done')

