from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.contrib import messages,auth

from django import forms
# Create your views here.

class LoginForm(forms.Form):
    username = forms.CharField(label='用户名', max_length=20, help_text='请输入您的用户名')
    password = forms.CharField(label='密码', widget=forms.PasswordInput())


def homepage(request):
    return render(request, 'homepage.html')


def login(request):
    if request.user.is_authenticated():
        messages.warning(request, '用户 {username}, 你已经登陆'.format(username=request.user.username))
        return HttpResponseRedirect('/')
    form = LoginForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        user = auth.authenticate(username=username, password=password)
        if user and user.is_active:
            auth.login(request, user)
            messages.success(request, '欢迎回来, {username}'.format(username=request.user.username))
            return HttpResponseRedirect('/')
        else:
            messages.error(request, '账号或密码错误')
    return render(request, 'login.html', {'login_form': form})

def logout(request):
    messages.success(request, '登出成功, Bye~')
    auth.logout(request)
    return HttpResponseRedirect('/')