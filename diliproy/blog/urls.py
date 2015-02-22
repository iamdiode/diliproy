from django.conf.urls import patterns, include, url

urlpatterns = patterns('blog.views',
	url(r'^$', 'archive', name='blog_home'),
	url(r'^post/(?P<slug>[-\w]+)/$', 'single_post', name='blog_post'),
	url(r'^category/(?P<slug>[-\w]+)/$', 'category_archive', name='category_archive'),
)