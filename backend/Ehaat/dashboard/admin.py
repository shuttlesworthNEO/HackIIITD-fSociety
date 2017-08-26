from django.contrib import admin
from .models import Sale, Inventory, ProductHit, StallHit

# Register your models here.
admin.site.register(Sale)
admin.site.register(Inventory)
admin.site.register(ProductHit)
admin.site.register(StallHit)
