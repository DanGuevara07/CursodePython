from django.urls import re_path as url
from catalog import views

urlpatterns = [
    url(r'^$', views.index, name='index')
]