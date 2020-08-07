from django.contrib import admin
from .models import serv, users, trans, cart 

# Register your models here.


admin.site.register(serv)
admin.site.register(users)
admin.site.register(trans)
admin.site.register(cart)