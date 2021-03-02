"""webPyAPI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path,include
from webPyAPI_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^$', views.index_page,name='index_page'),
    re_path(r'^about',views.about_page,name='about_page'),
    re_path(r'^converter',views.converter,name='converter'),
    re_path(r'^code',views.code_page,name='code_page'),
    re_path(r'^check_data',views.check_data,name='check_data'),
    re_path(r'^test_template',views.test_template,name='test_template'),
    re_path(r'^generate_csv',views.generate_csv,name='generate_csv'),
    re_path(r'^wordcloud',views.wordcloud,name='wordcloud'),
    re_path(r'^get_wordcloud',views.get_wordcloud,name='get_wordcloud'),

    #re_path(r'^webPyAPI_app/',include('webPyAPI_app.urls')),

]
