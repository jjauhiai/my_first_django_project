#from django.conf.urls import patterns, include, url
#from hello.views import foo
#from django.conf.urls import *
#from django.contrib import admin
#admin.autodiscover()
from django.conf.urls import url
from django.shortcuts import render
from django.contrib import admin
from . import views


urlpatterns=[
    # Examples:
    # url(r'^$', 'HelloWorld.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
    url(r'^foo$', views.foo, name='foo'),
    url(r'^bar$', views.bar, name='bar'),
    url(r'^hell$', views.hell,name='hello'),
    url(r'^post_list$', views.post_list,name='post_list'),
    url(r'^admin/', admin.site.urls)
]
