from django.conf.urls import url
from .views import haatList, stallList, productList, haatSingle

urlpatterns = [
	url(r'api/haats', haatList),
	url(r'api/haat/(?P<haatID>\w+)', haatSingle)
	url(r'api/stall', stallList),
	url(r'api/product', productList),
]