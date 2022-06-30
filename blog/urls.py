from django.urls import re_path
from blog.views import post_list, post_detail

urlpatterns = [
    re_path(r'^$', post_list, name='post_list'),
    re_path(r'^post/(?P<pk>[0-9]+)/$', post_detail, name='post_detail'),
]