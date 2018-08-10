# -*- coding: UTF-8 -*-
# author= YQZHU

from django.conf.urls import url, include
from django.contrib import admin

from . import sales_views

urlpatterns = [
    # Sales
    url(r'^add_client$', sales_views.add_client, name='add_client'),
    # url(r'^list_user', views.list_user, name='list_user'),
    # url(r'^reset_pwd/(?P<id>[0-9]+)$', views.reset_pwd, name='reset_pwd'),
    # url(r'^update_perm/(?P<id>[0-9]+)$', views.update_perm, name='update_perm'),


]