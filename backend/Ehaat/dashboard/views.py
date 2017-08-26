from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from details.models import Stall, Product
import datetime
import json
from .models import Sale, Inventory, ProductHit, StallHit

# Create your views here.

def dash(request, stallID):
	stall = Stall.objects.get(id = stallID)
	products = Product.objects.filter(stall = stallID)
	inventory = Inventory.objects.filter(stall = stallID)
	return render(request, 'dashboard/index.html', {"stallData" : stall, "productData" : products, "inventoryData" : inventory})

@csrf_exempt
def prodHits(request):
	if request.method == "POST":
		data = json.loads(request.body.decode(encoding='UTF-8'))
		productID = data["productID"]
		stallID = data["stallID"]
		ProductHit.objects.create(product=productID, stall=stallID)
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
		stalHits.objects.create(stall=stallID)
		jsonObj = {
			'code' : 200,
		}
		return JsonResponse(jsonObj, safe=False)
	else:
		jsonObj = {
			'code' : 400,
		}
		return JsonResponse(jsonObj, safe=False)


