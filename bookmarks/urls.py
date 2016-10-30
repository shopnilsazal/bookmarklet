from django.conf.urls import url
from .views import index, show_category

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^category/(?P<category_slug>[\w\-]+)/$', show_category, name='show_category')
]
