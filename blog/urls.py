from django.urls import re_path
from blog.views import post_list

urlpatterns = [
    re_path(r'^$', post_list, name='post_list'),
]