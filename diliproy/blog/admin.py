from django.contrib import admin
from django_markdown.admin import MarkdownModelAdmin
from .models import BlogPost, Tag


class TagAdmin(admin.ModelAdmin):
	class Meta:
		model = Tag


class BlogPostAdmin(MarkdownModelAdmin):
	date_hierarchy = "created"
	list_display = ("title", "publish", "created")
	search_fields = ("title",)
	prepopulated_fields = {"slug": ("title",)}
	readonly_fields = ("created", "updated")

	class Meta:
		model = BlogPost


admin.site.register(BlogPost, BlogPostAdmin)		
admin.site.register(Tag, TagAdmin)