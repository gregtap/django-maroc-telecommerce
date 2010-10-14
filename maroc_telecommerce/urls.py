from django.conf.urls.defaults import *

urlpatterns = patterns('maroc_telecommerce.views',
    url(r'^callback/$', 'callback', name='doffer_callback'),
)
