from django.contrib import admin

from cart.models import *

admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Order)
