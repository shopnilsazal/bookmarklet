from django import template
from bookmarks.models import Category

register = template.Library()


@register.inclusion_tag('cats.html')
def get_all_categories(cat=None):
    return {'categories': Category.objects.all(), 'act_cat': cat}
