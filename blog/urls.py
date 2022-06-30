from django.urls import re_path
from blog.views import post_list, post_detail, post_new, post_edit

urlpatterns = [
    re_path(r'^$', post_list, name='post_list'),
    re_path(r'^post/(?P<pk>[0-9]+)/$', post_detail, name='post_detail'),
    re_path(r'^post/new/$', post_new, name='post_new'),
    re_path(r'^post/(?P<pk>[0-9]+)/edit/$', post_edit, name='post_edit'),

]