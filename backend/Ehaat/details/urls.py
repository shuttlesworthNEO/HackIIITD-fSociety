from django.conf.urls import url
from .views import haatList, haatSingle

urlpatterns = [
	url(r'api/haats', haatList),
	url(r'api/haat/(?P<haatID>\w+)', haatSingle)
]