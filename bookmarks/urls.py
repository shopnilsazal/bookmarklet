from django.conf.urls import url
from .views import index, show_category, add_category, add_page, register, \
    user_login, user_logout, track_url, like_category, suggest_category

app_name = 'bookmarks'

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^add-category/$', add_category, name='add_category'),
    url(r'^category/(?P<category_slug>[\w\-]+)/add-page/$', add_page, name='add_page'),
    url(r'^category/(?P<category_slug>[\w\-]+)/$', show_category, name='show_category'),
    url(r'^register/$', register, name='register'),
    url(r'^login/$', user_login, name='login'),
    url(r'^logout/$', user_logout, name='logout'),
    url(r'^goto/$', track_url, name='goto'),
    url(r'^like/$', like_category, name='like'),
    url(r'^suggest/$', suggest_category, name='suggest_category')
]

