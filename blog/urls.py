from django.conf.urls import url, include
from django.contrib import admin
from . import views

app_name = 'blog'
urlpatterns = [

    url(r'^$', views.index, name='index'),
    url(r'^(?P<tag>\w+)/$', views.blog, name='blog'),
    url(r'^article/(?P<id>[1-9]+)/$', views.article, name='article'),

]
