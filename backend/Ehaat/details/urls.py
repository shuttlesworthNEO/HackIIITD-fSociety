from django.conf.urls import url
from .views import haatList, stallList, productList, haatSingle, stallSingle, productSingle

urlpatterns = [
	url(r'api/haats', haatList),
	url(r'api/haat/(?P<haatID>\w+)', haatSingle),
	url(r'api/stall/(?P<stallID>\w+)', stallSingle),
	url(r'api/product/(?P<productID>\w+)', productSingle),
	url(r'api/stall', stallList),
	url(r'api/product', productList),
]