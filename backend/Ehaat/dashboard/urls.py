from django.conf.urls import url
from .views import dash, prodHits, stalHits

urlpatterns = [
	url(r'(?P<stallID>\w+)', dash),
	url(r'api/prodhit', prodHits),
	url(r'api/stalhit', stalHits),
]