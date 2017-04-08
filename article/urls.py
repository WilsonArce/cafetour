from django.conf.urls import include, url
from article import views as myapp_views

urlpatterns = [
	url(r'^index/', myapp_views.index, name='index'),
]