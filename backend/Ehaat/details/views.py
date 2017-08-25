from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse
from django.core.serializers import serialize
from .models import Haat, Stall, Product
# Create your views here.

def haatList(request):
	haats = Haat.objects.all()
	jsonObj = []
	for haat in haats:
		temp = dict()
		temp["haatID"] = haat.id
		temp["name"] = haat.name
		temp["theme"] = haat.theme
		temp["info"] = haat.info
		temp["address"] = haat.address
		jsonObj.append(temp)
	return JsonResponse({"haats" : jsonObj})

def stallList(request):
	stalls = Stall.objects.all()
	jsonObj = []
	for stall in stalls:
		temp = dict()
		temp["haatID"] = stall.haat
		temp["stallID"] = stall.id
		temp["name"] = stall.name
		temp["stallNumber"] = stall.stallNumber
		temp["story"] = stall.story
		temp["tags"] = stall.tags.split(',')
		jsonObj.append(temp)
	return JsonResponse({"stalls" : jsonObj}, safe=False)

def productList(request):
	products = Product.objects.all()
	jsonObj = []
	for product in products:
		temp = dict()
		temp["stallID"] = product.stall
		temp["productID"] = product.id
		temp["name"] = product.name
		temp["description"] = product.description
		temp["price"] = product.price
		temp["promotions"] = product.promotions
		jsonObj.append(temp)
	return JsonResponse({'products' : temp}, safe=False)

def haatSingle(request, haatID):
	try:
		haat = Haat.objects.get(id = haatID)
	except Exception as e:
		print(e)
		haat = None
	if haat:
		temp = dict()
		temp["haatID"] = haat.id
		temp["name"] = haat.name
		temp["theme"] = haat.theme
		temp["info"] = haat.info
		temp["address"] = haat.address
		return JsonResponse({"haat" : temp})
	else:
		return JsonResponse({"error" : True})