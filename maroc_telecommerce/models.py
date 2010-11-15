# -*- coding: utf-8 -*-
from django.db import models
from django.conf import settings
from  maroc_telecommerce import settings  

from restkit import Resource
import urllib
import urllib2, httplib
import hashlib 


COUNTRY_CHOICES = (
    ('AC','Ascension Island'),
    ('AD','Andorra'),
    ('AE','United Arab Emirates'),
    ('AF','Afghanistan'),
    ('AG','Antigua and Barbuda'),
    ('AI','Anguilla'),
    ('AL','Albania'),
    ('AM','Armenia'),
    ('AN','Netherlands Antilles'),
    ('AO','Angola'),
    ('AQ','Antarctica'),
    ('AR','Argentina'),
    ('AS','American Samoa'),
    ('AT','Austria'),
    ('AU','Australia'),
    ('AW','Aruba'),
    ('AX','Aland Islands'),
    ('AZ','Azerbaijan'),
    ('BA','Bosnia and Herzegovina'),
    ('BB','Barbados'),
    ('BD','Bangladesh'),
    ('BE','Belgium'),
    ('BF','Burkina Faso'),
    ('BG','Bulgaria'),
    ('BH','Bahrain'),
    ('BI','Burundi'),
    ('BJ','Benin'),
    ('BM','Bermuda'),
    ('BN','Brunei Darussalam'),
    ('BO','Bolivia'),
    ('BR','Brazil'),
    ('BS','Bahamas'),
    ('BT','Bhutan'),
    ('BV','Bouvet Island'),
    ('BW','Botswana'),
    ('BY','Belarus'),
    ('BZ','Belize'),
    ('CA','Canada'),
    ('CC','Cocos (Keeling) Islands'),
    ('CD','Congo, Democratic Republic'),
    ('CF','Central African Republic'),
    ('CG','Congo'),
    ('CH','Switzerland'),
    ('CI',"Cote D'Ivoire (Ivory Coast)"),
    ('CK','Cook Islands'),
    ('CL','Chile'),
    ('CM','Cameroon'),
    ('CN','China'),
    ('CO','Colombia'),
    ('CR','Costa Rica'),
    ('CS','Czechoslovakia (former)'),
    ('CU','Cuba'),
    ('CV','Cape Verde'),
    ('CX','Christmas Island'),
    ('CY','Cyprus'),
    ('CZ','Czech Republic'),
    ('DE','Germany'),
    ('DJ','Djibouti'),
    ('DK','Denmark'),
    ('DM','Dominica'),
    ('DO','Dominican Republic'),
    ('DZ','Algeria'),
    ('EC','Ecuador'),
    ('EE','Estonia'),
    ('EG','Egypt'),
    ('EH','Western Sahara'),
    ('ER','Eritrea'),
    ('ES','Spain'),
    ('ET','Ethiopia'),
    ('FI','Finland'),
    ('FJ','Fiji'),
    ('FK','Falkland Islands (Malvinas)'),
    ('FM','Micronesia'),
    ('FO','Faroe Islands'),
    ('FR','France'),
    ('FX','France, Metropolitan'),
    ('GA','Gabon'),
    ('GB','Great Britain (UK)'),
    ('GD','Grenada'),
    ('GE','Georgia'),
    ('GF','French Guiana'),
    ('GG','Guernsey'),
    ('GH','Ghana'),
    ('GI','Gibraltar'),
    ('GL','Greenland'),
    ('GM','Gambia'),
    ('GN','Guinea'),
    ('GP','Guadeloupe'),
    ('GQ','Equatorial Guinea'),
    ('GR','Greece'),
    ('GS','S. Georgia and S. Sandwich Isls.'),
    ('GT','Guatemala'),
    ('GU','Guam'),
    ('GW','Guinea'),
    ('GY','Guyana'),
    ('HK','Hong Kong'),
    ('HM','Heard and McDonald Islands'),
    ('HN','Honduras'),
    ('HR','Croatia (Hrvatska)'),
    ('HT','Haiti'),
    ('HU','Hungary'),
    ('ID','Indonesia'),
    ('IE','Ireland'),
    ('IL','Israel'),
    ('IM','Isle of Man'),
    ('IN','India'),
    ('IO','British Indian Ocean Territory'),
    ('IQ','Iraq'),
    ('IR','Iran'),
    ('IS','Iceland'),
    ('IT','Italy'),
    ('JE','Jersey'),
    ('JM','Jamaica'),
    ('JO','Jordan'),
    ('JP','Japan'),
    ('KE','Kenya'),
    ('KG','Kyrgyzstan'),
    ('KH','Cambodia'),
    ('KI','Kiribati'),
    ('KM','Comoros'),
    ('KN','Saint Kitts and Nevis'),
    ('KP','Korea (North)'),
    ('KR','Korea (South)'),
    ('KW','Kuwait'),
    ('KY','Cayman Islands'),
    ('KZ','Kazakhstan'),
    ('LA','Laos'),
    ('LB','Lebanon'),
    ('LC','Saint Lucia'),
    ('LI','Liechtenstein'),
    ('LK','Sri Lanka'),
    ('LR','Liberia'),
    ('LS','Lesotho'),
    ('LT','Lithuania'),
    ('LU','Luxembourg'),
    ('LV','Latvia'),
    ('LY','Libya'),
    ('MA','Morocco'),
    ('MC','Monaco'),
    ('MD','Moldova'),
    ('ME','Montenegro'),
    ('MG','Madagascar'),
    ('MH','Marshall Islands'),
    ('MK','F.Y.R.O.M. (Macedonia)'),
    ('ML','Mali'),
    ('MM','Myanmar'),
    ('MN','Mongolia'),
    ('MO','Macau'),
    ('MP','Northern Mariana Islands'),
    ('MQ','Martinique'),
    ('MR','Mauritania'),
    ('MS','Montserrat'),
    ('MT','Malta'),
    ('MU','Mauritius'),
    ('MV','Maldives'),
    ('MW','Malawi'),
    ('MX','Mexico'),
    ('MY','Malaysia'),
    ('MZ','Mozambique'),
    ('NA','Namibia'),
    ('NC','New Caledonia'),
    ('NE','Niger'),
    ('NF','Norfolk Island'),
    ('NG','Nigeria'),
    ('NI','Nicaragua'),
    ('NL','Netherlands'),
    ('NO','Norway'),
    ('NP','Nepal'),
    ('NR','Nauru'),
    ('NT','Neutral Zone'),
    ('NU','Niue'),
    ('NZ','New Zealand (Aotearoa)'),
    ('OM','Oman'),
    ('PA','Panama'),
    ('PE','Peru'),
    ('PF','French Polynesia'),
    ('PG','Papua New Guinea'),
    ('PH','Philippines'),
    ('PK','Pakistan'),
    ('PL','Poland'),
    ('PM','St. Pierre and Miquelon'),
    ('PN','Pitcairn'),
    ('PR','Puerto Rico'),
    ('PS','Palestinian Territory, Occupied'),
    ('PT','Portugal'),
    ('PW','Palau'),
    ('PY','Paraguay'),
    ('QA','Qatar'),
    ('RE','Reunion'),
    ('RO','Romania'),
    ('RS','Serbia'),
    ('RU','Russian Federation'),
    ('RW','Rwanda'),
    ('SA','Saudi Arabia'),
    ('SB','Solomon Islands'),
    ('SC','Seychelles'),
    ('SD','Sudan'),
    ('SE','Sweden'),
    ('SG','Singapore'),
    ('SH','St. Helena'),
    ('SI','Slovenia'),
    ('SJ','Svalbard & Jan Mayen Islands'),
    ('SK','Slovak Republic'),
    ('SL','Sierra Leone'),
    ('SM','San Marino'),
    ('SN','Senegal'),
    ('SO','Somalia'),
    ('SR','Suriname'),
    ('ST','Sao Tome and Principe'),
    ('SU','USSR (former)'),
    ('SV','El Salvador'),
    ('SY','Syria'),
    ('SZ','Swaziland'),
    ('TC','Turks and Caicos Islands'),
    ('TD','Chad'),
    ('TF','French Southern Territories'),
    ('TG','Togo'),
    ('TH','Thailand'),
    ('TJ','Tajikistan'),
    ('TK','Tokelau'),
    ('TM','Turkmenistan'),
    ('TN','Tunisia'),
    ('TO','Tonga'),
    ('TP','East Timor'),
    ('TR','Turkey'),
    ('TT','Trinidad and Tobago'),
    ('TV','Tuvalu'),
    ('TW','Taiwan'),
    ('TZ','Tanzania'),
    ('UA','Ukraine'),
    ('UG','Uganda'),
    ('UK','United Kingdom'),
    ('UM','US Minor Outlying Islands'),
    ('US','United States'),
    ('UY','Uruguay'),
    ('UZ','Uzbekistan'),
    ('VA','Vatican City State (Holy See)'),
    ('VC','Saint Vincent & the Grenadines'),
    ('VE','Venezuela'),
    ('VG','British Virgin Islands'),
    ('VI','Virgin Islands (U.S.)'),
    ('VN','Viet Nam'),
    ('VU','Vanuatu'),
    ('WF','Wallis and Futuna Islands'),
    ('WS','Samoa'),
    ('XK','Kosovo*'),
    ('YE','Yemen'),
    ('YT','Mayotte'),
    ('YU','Yugoslavia (former)'),
    ('ZA','South Africa'),
    ('ZM','Zambia'),
    ('ZR','Zaire'),
    ('ZW','Zimbabwe'),
)


class DigitalOffer(models.Model):
    """
    Maroc Telecommerce (spec v1.9) Digital Offer Model 
    """
    
    store_id = models.IntegerField(default=settings.STORE_ID, help_text="Store Identificant assigned by Maroc Telecommerce")
    langue = models.CharField(max_length=2, default=settings.LANG, blank=False, null=False, help_text="The language used during the Order Form display.")
    offer_url = models.CharField(max_length=200, help_text="The path that allows the buyer to return to the store.")
    update_url = models.CharField(max_length=200, blank=True, help_text="The path that allows MarocTelecommerce to confirm the authorisation.")
    buyer_name = models.CharField(max_length=100, blank=True, help_text="Customer Last Name (and first name)")
    address = models.CharField(max_length=200, blank=True, help_text="Customer’s address")
    city = models.CharField(max_length=30, blank=True, help_text="Customer’s city")
    state = models.CharField(max_length=30, blank=True, help_text="Customer’s State/Province")
    country = models.CharField(max_length=2, choices=COUNTRY_CHOICES, blank=True, help_text="Customer’s country (must respect the annex’s list).")
    postcode = models.IntegerField(blank=True, null=True, help_text="Customer’s postal code")
    phone = models.CharField(max_length=30, blank=True, help_text="Customer’s phone number")
    email = models.EmailField(blank=True, help_text="Customer’s email address")
    checksum = models.CharField(max_length=32, blank=True, help_text="MD5 generated control code.")

    cart_id = models.CharField(unique=True, max_length=50, help_text="Optional : Order n° in the merchant site’s DB. If doesn’t exist = 0")
    mode = models.CharField(max_length=3, default='TAC', help_text=""""Order confirmation mode TAC / EXP""")  
    count = models.IntegerField(blank=True, null=True, default=1, help_text="Order articles count, he number of lines of the shopping cart")
    desc = models.TextField(help_text="Order articles descritions (desc1;desc2;...;descN with N=count=Order articles count)")
    qty = models.TextField(help_text="quantity of each order article (qty1;qty2;...;qtyN with N=count=Order articles count)")

    items_price = models.TextField(help_text="Order articles prices (price1;price2;...;priceN with N=count=Order articles count) en DH")
    amount_tx = models.FloatField(help_text="The transaction total amount without shipping charge (total price = price1+price2+...+priceN)")
    
    # should be optional but gives a 500 eror if not present
    shipping_charge = models.FloatField(default=0, help_text="Product shipping charge (if not included in the total amount)")
    
    shipping_weight = models.FloatField(blank=True, null=True, default=0, help_text="Product weight if shipping charge is calculated by Maroc telecommerce") 
    total_amount_tx = models.FloatField(help_text="AmountTx +ShippingCharge") 
    total_amount_cur = models.FloatField(blank=True, null=True, help_text="Foreign currency TotalmountTX equivalent.")
    symbol_cur = models.CharField(blank=True, max_length=5, help_text="Currency symbol to be shown on payment screens")

    multi_payment = models.BooleanField(default=True,  help_text="Authorize or not the payment of multiple caddies.")

    created = models.DateTimeField(editable=False, auto_now_add=True) 
    requested = models.BooleanField(default=False)
    test_mode = models.BooleanField(default=True, blank=True, help_text="Are we using the test gateway.") 


    def __unicode__(self):
        return "buyer: %s, email: %s, cart_id: %s, total: %s, date: %s" % (
            self.buyer_name, self.email, self.cart_id, self.total_amount_tx, self.created)

        
    def get_endpoint(self):
        """
        Set Sandbox endpoint if depending on test mode.
        """
 
        if self.test_mode:
            return settings.GATEWAY_TEST_URL
        else:
            return settings.GATEWAY_URL
                    
    def _checksum(self):
        """
        Calculate checksum as explained in the specs: 
        MD5(urlencode(utf8(form action + StoreId + CartId + Count + 
        TotalamounTx + Email + Secret Key)
        """
        if not self.email:
            email = ""
        else:
            email = self.email
 
        base_string = '%s%s%s%s%s%s%s' %(
                self.get_endpoint(), 
                self.store_id, 
                self.cart_id, 
                self.count, 
                self.total_amount_tx, 
                email,
                settings.SECRET
        )
        m = hashlib.md5()
        url = urllib.quote(base_string.encode( "utf-8" ), "")
 
        m.update(url)
        return m.hexdigest()
  
        
    def submit(self):
        """
        Performs an order (HTTP POST) on the gateway
        """
        if self.total_amount_cur == None:
            total_amount_cur = ""
        else:
            total_amount_cur = self.total_amount_cur
            
        values = {
            'StoreId': self.store_id,
            'Langue': self.langue,
            'OfferURL': self.offer_url,
            'UpdateURL': self.update_url,
            'CartId': self.cart_id,
            'Mode': self.mode,
            'Count': self.count,
            'Desc': self.desc, 
            'Qty': self.qty,
            'ItmesPrices': self.items_price,
            'AmountTX': self.amount_tx,
            'ShippingCharge': self.shipping_charge,
            'ShippingWeight': self.shipping_weight,
            'TotalmountTx': self.total_amount_tx,
            'TotalamountCur':  total_amount_cur,
            'SymbolCur': self.symbol_cur,
            'MultiPayment': self.multi_payment,
            'BuyerName': self.buyer_name,
            'Address': self.address,
            'City': self.city,
            'State': self.state,
            'Country': self.country,
            'Postcode': self.postcode,
            'Tel': self.phone, 
            'Email': self.email,
            'Checksum': self._checksum(),
        }
        
        data = _unicode_urlencode(values)
        res = Resource(self.get_endpoint())
        r = res.post(payload=data, headers={'Content-Type': 'application/x-www-form-urlencoded'})
        return r 
 

def _unicode_urlencode(params):
    """
    A unicode aware version of urllib.urlencode.
    """
    if isinstance(params, dict):
        params = params.items()
    return urllib.urlencode([(k, isinstance(v, unicode) and v.encode('utf-8') or v)
                      for k, v in params])    
         
    
