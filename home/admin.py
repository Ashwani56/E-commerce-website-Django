from django.contrib import admin
from home.models import Contact
from home.models import Customer
from home.models import Product
from home.models import Cart
from home.models import Cartitems
from home.models import ShippingAddress

from home.models import Table



admin.site.register(Contact)

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Cartitems)
admin.site.register(ShippingAddress)
admin.site.register(Table)




