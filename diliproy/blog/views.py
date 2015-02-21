from django.shortcuts import render
from .models import BlogPost


def archive(request):
	posts = BlogPost.objects.filter(publish=True)
	context = {"posts": posts}
	template = "blog/index.html"
	return render(request, template, context)
