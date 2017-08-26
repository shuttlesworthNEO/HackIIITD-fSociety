from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from details.models import Stall, Product
import datetime
import json
from .models import Sale, Inventory, ProductHit, StallHit
from django.db.models import Count, Sum

# Create your views here.

def dash(request, stallID):
	stall = Stall.objects.get(id = stallID)
	products = Product.objects.filter(stall = stallID)
	inventory = Inventory.objects.filter(stall = stallID)
	stallHits = StallHit.objects.filter(id = stallID)
	sales = Sale.objects.filter(stall = stallID)
	totalSold = sales.count()
	totalSales = sales.aggregate(Sum('salePrice'))["salePrice__sum"]
	salesDif = dict()
	# print(totalSold, totalSales)
	prodHits = dict()
	for prod in products:
		hits = ProductHit.objects.filter(stall = stallID, product = prod.id).count()
		total = Sale.objects.filter(stall = stallID, product = prod.id).count()
		prodHits[prod.name] = hits
		salesDif[prod.name] = total
	return render(request, 'dashboard/index.html', {"stallData" : stall, "productData" : products, "inventoryData" : inventory, "prodHits" : prodHits, "stallHits" : stallHits, "totalSold" : totalSold, "totalSales" : totalSales, "salesDif" : salesDif})

@csrf_exempt
def prodHits(request):
	if request.method == "POST":
		data = json.loads(request.body.decode(encoding='UTF-8'))
		productID = int(data["productID"])
		stallID = int(data["stallID"])
		prod = Product.objects.get(id = productID)
		stall = Stall.objects.get(id = stallID)
		obj = ProductHit(product=prod, stall=stall)
		obj.save()
		jsonObj = {
			'code' : 200,
		}
		return JsonResponse(jsonObj, safe=False)
	else:
		jsonObj = {
			'code' : 400,
		}
		return JsonResponse(jsonObj, safe=False)

@csrf_exempt
def stalHits(request):
	if request.method == "POST":
		data = json.loads(request.body.decode(encoding='UTF-8'))
		stallID = data["stallID"]
		stall = Stall.objects.get(id = stallID)
		StallHit.objects.create(stall = stall)
		jsonObj = {
			'code' : 200,
		}
		return JsonResponse(jsonObj, safe=False)
	else:
		jsonObj = {
			'code' : 400,
		}
		return JsonResponse(jsonObj, safe=False)


