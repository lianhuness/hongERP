# -*- coding: UTF-8 -*-
# author= YQZHU
from django.shortcuts import render, HttpResponse, HttpResponseRedirect, redirect,reverse,get_object_or_404
from django.contrib import messages,auth
from django.core.exceptions import ValidationError
from django.contrib.auth.decorators import permission_required, login_required
from django.contrib.auth.models import User, Permission, Group

from .sales_models import Client

@permission_required('team.add_client')
def my_clients(request):
    clients = request.user.client_set.all()
    return render(request, 'sales/my_clients.html', {'clients': clients})

from django.forms import ModelForm

class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(ClientForm, self).__init__(*args, **kwargs)  # populates the post
        salesGroup = Group.objects.get(name='SALES')
        self.fields['sales'].queryset = salesGroup.user_set.all()

@permission_required('team.add_client')
def add_client(request):
    if request.method == "POST":
        form = ClientForm(request.POST)
        if form.is_valid():
            client = form.save()
            messages.success(request, '客户添加成功:%s'%client.name )
            return redirect(reverse("view_client", kwargs={'id': client.id }))
    else:
        form = ClientForm()
        form.fields['sales'].initial = request.user

    return render(request, 'sales/add_client.html', {'form': form })

@permission_required('team.add_client')
def edit_client(request, id):
    client = get_object_or_404(Client, pk=id)
    if request.method == "POST":
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            client = form.save()
            messages.success(request, '客户修改成功:%s'%client.name )
            return redirect(reverse("view_client", kwargs={'id': client.id }))
    else:
        form = ClientForm(instance=client)

    return render(request, 'sales/edit_client.html', {'form': form, 'client': client })

@permission_required('team.add_client')
def view_client(request, id):
    client = get_object_or_404(Client, pk=id)
    if client.sales  == request.user:
        return render(request, 'sales/view_client.html', {'client': client})
    else:
        return HttpResponse('不是你的客户， 没有权限!')