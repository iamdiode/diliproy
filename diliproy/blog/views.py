from django.shortcuts import render
from django.views import generic
from .models import Entry


class BlogIndex(generic.ListView):
	queryset = Entry.objects.published()
	template = "blog/index.html"
	paginate_by = 4
