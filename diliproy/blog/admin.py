from django.contrib import admin
from django_markdown.admin import MarkdownModelAdmin
from .models import Entry


class EntryAdmin(MarkdownModelAdmin):
	date_hierarchy = "created"
	list_display = ("title", "slug", "created", "publish")
	search_fields = ("title", "created")
	prepopulated_fields = {"slug": ("title",)}
	readonly_fields = ["created", "updated"]

	class Meta:
		model = Entry

admin.site.register(Entry, EntryAdmin)		
