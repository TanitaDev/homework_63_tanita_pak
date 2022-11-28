from django.urls import path

from posts.views.base import IndexView
from posts.views.search import SearchView
from posts.views.posts import AddPost

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('add-post', AddPost.as_view(), name='add_post'),
    path('search', SearchView.as_view(), name='search')
]
