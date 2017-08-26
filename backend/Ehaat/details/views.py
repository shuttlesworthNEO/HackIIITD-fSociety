from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse
from django.core.serializers import serialize
from .models import Haat, Stall, Product, Rating
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
		temp["haatID"] = stall.haat.id
		temp["stallID"] = stall.id
		temp["name"] = stall.name
		temp["stallNumber"] = stall.stallNumber
		temp["story"] = stall.story
		temp["tags"] = stall.tags.split(',')
		temp["imageURL"] = stall.imageURL
		temp["ratings"] = []
		ratings = Rating.objects.filter(stall = stall.id)
		if ratings:
			for rating in ratings:
				rt = dict()
				rt["userName"] = rating.userName
				rt["value"] = rating.value
				rt["text"] = rating.text
				temp["ratings"].append(rt)
		jsonObj.append(temp)
	return JsonResponse({"stalls" : jsonObj}, safe=False)

def productList(request):
	products = Product.objects.all()
	jsonObj = []
	for product in products:
		temp = dict()
		temp["stallID"] = product.stall.id
		temp["productID"] = product.id
		temp["name"] = product.name
		temp["description"] = product.description
		temp["price"] = product.price
		temp["promotions"] = product.promotions
		temp["imageURL"] = product.imageURL
		jsonObj.append(temp)
	return JsonResponse({'products' : jsonObj}, safe=False)

# def stallRatings(request, stallID):
# 	try:
# 		ratings = Rating.objects.filter(stall.id = stallID)
# 	except Exception as e:
# 		print(e)
# 		ratings = None
# 	if ratings:
# 		jsonObj = []
# 		for rating in ratings:
# 			temp = dict()
# 			temp[""]

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

def stallSingle(request, stallID):
	try:
		stall = Stall.objects.get(id = stallID)
	except Exception as e:
		print(e)
		stall = None
	if stall:
		temp = dict()
		temp["haatID"] = stall.haat.id
		temp["stallID"] = stall.id
		temp["name"] = stall.name
		temp["stallNumber"] = stall.stallNumber
		temp["story"] = stall.story
		temp["tags"] = stall.tags.split(',')
		temp["imageURL"] = stall.imageURL
		ratings = Rating.objects.filter(stall = stallID)
		temp["ratings"] = []
		if ratings:
			for rating in ratings:
				rt = dict()
				rt["userName"] = rating.userName
				rt["value"] = rating.value
				rt["text"] = rating.text
				temp["ratings"].append(rt)
		return JsonResponse({"stall" : temp})
	else:
		return JsonResponse({"error" : True})

def productSingle(request, productID):
	try:
		product = Product.objects.get(id = productID)
	except Exception as e:
		print(e)
		product = None
	if product:
		temp = dict()
		temp["stallID"] = product.stall.id
		temp["productID"] = product.id
		temp["name"] = product.name
		temp["description"] = product.description
		temp["price"] = product.price
		temp["promotions"] = product.promotions
		temp["imageURL"] = product.imageURL
		return JsonResponse({"product" : temp})
	else:
		return JsonResponse({"error" : True})