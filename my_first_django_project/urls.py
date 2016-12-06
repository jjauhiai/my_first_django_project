#from django.conf.urls import patterns, include, url
from django.conf.urls import include, url
import django.contrib.auth.views
from django.contrib import admin
urlpatterns = [
     url(r'^admin/', include(admin.site.urls)),
     url(r'', include('hello.urls')),
     url(r'^home/$', django.contrib.auth.views.login, name='login'),
]
