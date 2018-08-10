# -*- coding: UTF-8 -*-
# author= YQZHU
from django.shortcuts import render, HttpResponse, HttpResponseRedirect, redirect,reverse,get_object_or_404
from django.contrib import messages,auth
from django.core.exceptions import ValidationError
from django.contrib.auth.decorators import permission_required, login_required
from django.contrib.auth.models import User, Permission


def add_client(request):
    return HttpResponse("Hello world")