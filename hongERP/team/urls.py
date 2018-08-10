# -*- coding: UTF-8 -*-
# author= YQZHU

from django.conf.urls import url, include
from django.contrib import admin

from . import sales_views

urlpatterns = [
    # Sales
    url(r'^my_clients$', sales_views.my_clients, name='my_clients'),
    url(r'^add_client$', sales_views.add_client, name='add_client'),
    url(r'^view_client/(?P<id>[0-9]+)$', sales_views.view_client, name='view_client'),
    url(r'^edit_client/(?P<id>[0-9]+)$', sales_views.edit_client, name='edit_client'),
    # url(r'^list_user', views.list_user, name='list_user'),
    # url(r'^reset_pwd/(?P<id>[0-9]+)$', views.reset_pwd, name='reset_pwd'),
    # url(r'^update_perm/(?P<id>[0-9]+)$', views.update_perm, name='update_perm'),


]