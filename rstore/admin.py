from django.contrib import admin
from .models import serv, msg, clin

# Register your models here.


admin.site.register(serv)
admin.site.register(msg)
admin.site.register(clin)