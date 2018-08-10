from django.shortcuts import render, HttpResponse, HttpResponseRedirect, redirect,reverse,get_object_or_404
from django.contrib import messages,auth
from django.core.exceptions import ValidationError
from django.contrib.auth.decorators import permission_required, login_required
from django.contrib.auth.models import User, Permission

# Create your views here.
from django import forms

class NewUserForm(forms.Form):
    username = forms.CharField(label='用户名', max_length=20, help_text='新用户的用户名')
    password = forms.CharField(label='密码', widget=forms.PasswordInput())
    real_name = forms.CharField(label='姓名', max_length=20, help_text='姓名')

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise ValidationError('用户名已经存在！')
        return username

@permission_required('auth.add_user')
def add_user(request):
    if request.method == 'POST':
        form =  NewUserForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(username=form.cleaned_data['username'], password=form.cleaned_data['password'],
                                     first_name=form.cleaned_data['real_name'])
            messages.success(request, '成功添加用户： %s'%(user.username))
            return redirect(reverse('list_user'))
    else:
        form = NewUserForm()
    return render(request, 'add_user.html', {'form': form})

@permission_required('auth.add_user')
def list_user(request):
    users = User.objects.filter(is_superuser=False).all()
    return render(request, 'list_user.html', {'users': users})

@permission_required('auth.add_user')
def reset_pwd(request, id):
    user = get_object_or_404(User, pk=id)
    if user.is_superuser:
        messages.error(request, "Cannot reset super user!")
    else:
        user.set_password('hongda')
        user.save()
        messages.success(request, 'User(%s) password has updated to "hongda" '%user.username)

    return redirect(reverse('list_user'))


@permission_required('auth.add_user')
def update_perm(request, id):
    if request.method == 'POST':
        user = get_object_or_404(User, pk=id)
        perm = request.POST.get('PERM')
        checked = request.POST.get('checked')
        if perm == 'ADMIN':
            permission = Permission.objects.get(codename='add_user')
            if checked == 'true':
                user.user_permissions.add(permission)
            else:
                user.user_permissions.remove(permission)
        else:
            return HttpResponse("错误")
        return HttpResponse("PERMISSION UPDATED SUCCESS!")
    return HttpResponse("错误")

class UserProfileForm(forms.Form):
    password = forms.CharField(label='密码', widget=forms.PasswordInput())
    real_name = forms.CharField(label='姓名', max_length=20, help_text='姓名')

@login_required
def user_profile(request):
    if request.method == 'POST':
        user = get_object_or_404(User, pk=request.user.id)
        form = UserProfileForm(request.POST)
        if form.is_valid():
            user.set_password(form.cleaned_data['password'])
            user.first_name = form.cleaned_data['real_name']
            user.save()
            messages.success(request, '用户信息更改成功')
            return HttpResponseRedirect('/')
    else:
        form = UserProfileForm()
        form.fields['real_name'].initial = request.user.first_name

    return render(request, 'user_profile.html', {'user': request.user, 'form': form})

