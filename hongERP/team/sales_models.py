# -*- coding: UTF-8 -*-
# author= YQZHU

from django.db import models
from django.contrib.auth.models import User, Permission



class Client(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    sales = models.ForeignKey(User, verbose_name='业务员')
    name = models.CharField(max_length=100, verbose_name='客户公司名称')
    district = models.CharField(max_length=100, verbose_name='地区')
    source = models.CharField(max_length=50, verbose_name='客户来源')
    note = models.TextField(verbose_name='其他')

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


