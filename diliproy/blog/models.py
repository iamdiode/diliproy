from django.db import models
from django_markdown.models import MarkdownField


class Tag(models.Model):
	tag = models.SlugField(unique=True)

	def __str__(self):
		return self.tag


class BlogPost(models.Model):
	title = models.CharField(max_length=120)
	body = MarkdownField()
	slug = models.SlugField(unique=True)
	tags = models.ManyToManyField(Tag)
	publish = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __str__(self):
		return self.title

	class Meta:
		ordering = ["-created"]
		unique_together = ("title", "slug")