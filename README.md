Django Maroc Telecommerce
=========================

Django Maroc Telecommerce is an application that implements Maroc Telecommerce
payment gateway. Is is based on their 1.9 specs. Basically it takes care of the
DigitalOffer (order) posting to the gateway as well as the callback handling. It uses Signals and HttpRedirects for optimal decoupling.

Each order made to the gateway is persisted to db.

http://www.maroctelecommerce.com/

Installation
------------

    pip install -e git@github.com:coulix/django-maroc-telecommerce.git#egg=dango-maroc-telecommerce

    # Restkit (HTTP lib)
    pip install -e git+http://github.com/benoitc/restkit.git#egg=restkit

Usage
-----

Add the app to you settings.py

    INSTALLED_APPS = (
        ...
        'maroc_telecommerce'
        ...
    )


Override the default callback in your urls.py to add your own redirect_url which
will be used for the http redirect once the payment is done

    urlpatterns += patterns('maroc_telecommerce.views',
        url(r'purchase/payment/maroc_telecommerce/callback/$', 'callback',
            name='maroc_doffer_callback', 
            kwargs={'redirect_url': '/purchase/completed'}),
    )


Submit an order

    from maroc_telecommerce.models import DigitalOffer
        ...
        digital_offer = DigitalOffer(cart_id=...)
        digital_offer.full_clean()
        digital_offer.submit()


    
Signals
-------

telecommerce_callback_received
    
+ **is_valid** : True if the POST data from the callback matches a saved
digital offer.

+ **is_payed** : True if the POST data result is 'ok'

+ **mtc_order_num** : Maroc telecommerce id

+ **order_id** : Your cart id 

+ **post_data** : The raw post data


Settings
--------

+ **GATEWAY_URL** : the production gateway url

+ **GATEWAY_TEST_URL** : test gateway url

+ **STORE_ID** : Your store id (provided by maroc telecommerce)

+ **SECRET** : Secret key (provided as well)

+ **LANG** : 'EN' or 'FR'



