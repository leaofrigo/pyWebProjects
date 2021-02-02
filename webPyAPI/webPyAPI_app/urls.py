from django.conf.urls import include
from django.urls import re_path
re_path(r'^$', views.index, name='index'),
re_path(r'^webPyAPI_app',include('webPyAPI_app.urls')),
