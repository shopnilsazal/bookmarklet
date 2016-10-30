from django.contrib import admin
from bookmarks.models import Category, Page

# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    fields = ['name', 'views', 'likes']
    list_display = ('name', 'views', 'likes')


class PageAdmin(admin.ModelAdmin):
    fields = ['title', 'category', 'url', 'views']
    list_display = ('title', 'category', 'url', 'views')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)
