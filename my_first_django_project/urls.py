#from django.conf.urls import patterns, include, url
from django.conf.urls import *

urlpatterns = [

    url(r'', include('hello.urls')),
]
