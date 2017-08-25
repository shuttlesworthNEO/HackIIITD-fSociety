from django.conf.urls import url
from .views import haatList

urlpatterns = [
	url(r'api/haat', haatList),
]