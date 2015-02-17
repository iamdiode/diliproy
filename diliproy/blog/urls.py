from django.conf.urls import url, patterns, include
from . import views

urlpatterns = patterns('',
	url(r'^$', views.BlogIndex.as_view(), name='Index'),
)