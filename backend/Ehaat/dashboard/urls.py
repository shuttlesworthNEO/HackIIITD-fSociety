from django.conf.urls import url
from .views import dash

urlpatterns = [
	url(r'(?P<stallID>\w+)', dash),
]