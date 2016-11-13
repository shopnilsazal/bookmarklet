from django.conf.urls import url
from .views import index, show_category, add_category, add_page

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^add-category/$', add_category, name='add_category'),
    url(r'^category/(?P<category_slug>[\w\-]+)/add-page/$', add_page, name='add_page'),
    url(r'^category/(?P<category_slug>[\w\-]+)/$', show_category, name='show_category')
]
