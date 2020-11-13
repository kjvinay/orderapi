from django.contrib import admin
from .models import company,product,order

admin.site.register(company)
admin.site.register(product)
admin.site.register(order)

