from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^post/new/$', views.post_new, name='post_new'),
	url(r'^imdb/$', views.imdb, name='imdb'),
]