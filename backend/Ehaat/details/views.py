from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse
from django.core.serializers import serialize
from .models import Haat
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