from django.shortcuts import render
from django.http import HttpResponseRedirect
from details.models import Stall, Product
from .models import Sale, Inventory, ProductHit, StallHit

# Create your views here.

def dash(request, stallID):
	stall = Stall.objects.get(id = stallID)
	products = Product.objects.filter(stall = stallID)
	inventory = Inventory.objects.filter(stall = stallID)
	return render(request, 'dashboard/index.html', {"stallData" : stall, "productData" : products, "inventoryData" : inventory})
