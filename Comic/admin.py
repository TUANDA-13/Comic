from xml.etree.ElementTree import Comment
from django.contrib import admin

# Register your models here.
from Comic.models import Category,Comic, RepComment,CommentComic
from Comic.models import Chapter, Page
# Register your models here.

admin.site.register(Category)
admin.site.register(Comic)
admin.site.register(Chapter)
admin.site.register(Page)
admin.site.register(CommentComic)
admin.site.register(RepComment)