from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import BlogPost, Category


def archive(request):
	posts = BlogPost.objects.all()
	paginator = Paginator(posts, 6)
	page = request.GET.get("page")
	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer deliver this page
		posts = paginator.page(1)
	except EmptyPage:
		# If page is out of range, deliver the last page in the result set
		posts = paginator.page(paginator.num_pages)
	categories = Category.objects.all()
	template = "blog/index.html"
	return render(request, template, locals())


def single_post(request, slug):
	post = get_object_or_404(BlogPost, slug=slug)
	categories = Category.objects.all()
	template = "blog/single.html"
	return render(request, template, locals())


def category_archive(request, slug):
	category = get_object_or_404(Category, slug=slug)
	categories = Category.objects.all()
	posts = BlogPost.objects.filter(category=category)
	paginator = Paginator(posts, 6)
	page = request.GET.get("page")
	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer deliver this page
		posts = paginator.page(1)
	except EmptyPage:
		# If page is out of range, deliver the last page in the result set
		posts = paginator.page(paginator.num_pages)
	template = "blog/category.html"
	return render(request, template, locals())

