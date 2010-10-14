#-*- coding: utf-8 -*-
from django.test.client import Client
from django.test import TestCase
 
from maroc_telecommerce.models import DigitalOffer
  

class OrderTest(TestCase):
    def setUp(self):
        self.client = Client()
  
    def test_order_simple(self):
        """
        Basic test
        """
        order = DigitalOffer(
            cart_id=46,
            total_amount_tx=2051.32,
            amount_tx=100.0,
            items_price="230",
            qty="3",
            desc="my product",
            offer_url="http://www.site_marchand.com",
            update_url="http://www.postbin.org/13xrjup",
        )

        order.full_clean()
        resp = order.submit()
        self.assertEqual(resp.status_int, 302) 
        
 
       
 
