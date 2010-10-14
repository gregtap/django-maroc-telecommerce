import django.dispatch  

telecommerce_callback_received = django.dispatch.Signal(
    providing_args=["is_valid", "is_payed", "mtc_order_num", "order_id",  "post_data"])
