from django.conf.urls import url, include, patterns
from .views import archive


urlpatterns = patterns('',
	url(r'^$', archive, name='blog_home'),
)