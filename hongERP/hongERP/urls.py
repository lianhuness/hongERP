"""hongERP URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from hongERP import settings

from page import views as pageview


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^admin/', admin.site.urls),
    url(r'^auth/', include([
        url(r'^login/$', pageview.login, name='login'),
        url(r'^logout/$', pageview.logout, name='logout'),
    ]), name='auth'),

    url(r'^$', pageview.homepage, name='homepage'),

    url(r'backend/', include('backend.urls')),
    url(r'pages/', include('page.urls')),
]+ static( settings.MEDIA_URL , document_root=settings.MEDIA_ROOT )
