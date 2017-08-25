from django.conf.urls import url
from .views import haatList, stallList, productList

urlpatterns = [
	url(r'api/haat', haatList),
	url(r'api/stall', stallList),
	url(r'api/product', productList),
]