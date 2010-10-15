 #-*- coding: utf-8 -*-
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_view_exempt
from django.views.decorators.http import require_POST
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

from maroc_telecommerce.models import DigitalOffer
from maroc_telecommerce.signals import telecommerce_callback_received


MAPPED_PARAMS_TO_CHECK = {
    'count':'count', 
    'city':'city',
    'StoreId':'store_id', 
    'tel':'phone',
    'cardName':'buyer_name',
    'country':'country',
    'qty':'qty', 
    'postcode':'postcode', 
    'address':'address', 
    'email':'email', 
    'TotalmountTx':'total_amount_tx',
    'desc':'desc'
}

@login_required
@require_POST
@csrf_view_exempt
def callback(request, template="maroc_telecommerce_callback.html", 
    success_redirect_url="",  failure_redirect_url=""): 
    """
    Call back from the gateway.
    We match the POST data received from maroc telecommerce to a potential 
    instance of DigitalOffer. 
    If no match is found or the match is erroneous we set is_valid to false 
    and dispatch a telecommerce_callback_received signal.
    We then redirect the user to a thanks page
    """
 
    is_valid = True
    is_payed = True
    order_submitted = None 
    mtc_order_num = None 
    
    cart_id = request.POST.get('cartId', None)
    
    if not cart_id:
        is_valid = False
     
    payment_result = request.POST.get('paymentResult', None)   
    if not payment_result or payment_result != "ok":
        is_valid = False
        is_payed = False
 
    try:
        order_submitted = DigitalOffer.objects.get(cart_id=cart_id)
    except DigitalOffer.DoesNotExist:
        is_valid = False
    
    if not _validate_digital_offer(request.POST, order_submitted):
        is_valid = False
      
    mtc_order_num = request.POST.get('mtc_order_num', None) 
 
    # dispatch !
 
    telecommerce_callback_received.send( 
        sender=order_submitted,
        is_valid=is_valid,
        is_payed=is_payed,
        mtc_order_num=mtc_order_num,
        post_data=request.POST,
    )
 
    if order_submitted:
        cart_id = order_submitted.cart_id
    else:
        cart_id = ""
        
    if not is_payed:
        return HttpResponseRedirect("%s?is_payed=%s&cart_id=%s&method=maroc_tele" % (
            failure_redirect_url, is_payed, cart_id))
    return HttpResponseRedirect(success_redirect_url)
    

def _validate_digital_offer(post_data, digital_offer):
    for key, value in  MAPPED_PARAMS_TO_CHECK.iteritems():
        param = post_data.get(key, None)
        if not param or param != str(digital_offer.__dict__[value]):
            return False
    return True

    
