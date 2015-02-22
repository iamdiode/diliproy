from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django_markdown.models import MarkdownField


class Category(models.Model):
	title = models.CharField(max_length=120)
	slug = models.SlugField(unique=True)
	description = MarkdownField()
	created = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse("category", args=[str(self.slug)])



class Tag(models.Model):
	tag = models.SlugField(unique=True)

	def __str__(self):
		return self.tag


class PostManager(models.Manager):
	def all(self):
		return super(PostManager, self).filter(publish=True)


class BlogPost(models.Model):
	title = models.CharField(max_length=120)
	body = MarkdownField()
	slug = models.SlugField(unique=True)
	category = models.ForeignKey(Category, related_name='categories')
	tags = models.ManyToManyField(Tag)
	publish = models.BooleanField(default=True)
	objects = PostManager()
	created = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse("post", args=[str(self.slug)])

	def get_previous_post(self):
		return self.get_previous_by_created()

	def get_next_post(self):
		return self.get_next_by_created()

	class Meta:
		ordering = ["-created"]
		unique_together = ("title", "slug")