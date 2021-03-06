"""penyediajasa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path,include
from acounts import views
from django.contrib.auth.views import LoginView, LogoutView
from django.conf import settings
from django.conf.urls import url,include
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('frondend.urls')),
    path('home/', include('home.urls')),
    path('pengelola/', include('pengelola.urls')),
    path('acounts/', include('acounts.urls')),
    path('login/', views.user_login, name='login'),
    path('keluar/', LogoutView.as_view(next_page='login'), name='keluar'),
    path('register/', views.register, name='register'),
    path('cregister/', include('acounts.urls'))
    # url(r'^acounts/',include('acounts.urls')),
    # url(r'^logout/$', views.user_logout, name='logout'),
    # url(r'^register/',views.register,name='registerin'),
    # url(r'^login/',views.user_login,name='user_login'),
]