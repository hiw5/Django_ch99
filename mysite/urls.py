"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.conf import settings
from django.urls import path, include, re_path
from mysite.views import HomeView, UserCreateView, UserCreateDoneTV
from django.views.static import serve
import os


from django.http import HttpResponse
from django.contrib.auth import logout
# from bookmark.views import BookmarkLV, BookmarkDV

from django.contrib.auth.views import LogoutView

def debug_logout(request):
    print(f"Method: {request.method}")
    logout(request)
    return HttpResponse("Logged out for debugging")

urlpatterns = [
    path('admin/', admin.site.urls),

    #path('accounts/logout/', debug_logout, name='logout'),  # 임시 추가
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register', UserCreateView.as_view(), name='register'),
    path('accounts/register/done/', UserCreateDoneTV.as_view(), name='register_done'),

    path('', HomeView.as_view(), name='home'),

    path('bookmark/', include('bookmark.urls')),
    path('blog/', include('blog.urls')),    
    path('practice/', include('practice.urls')),

    path('api/', include('API.urls')),

]

if settings.DEBUG:
    urlpatterns += [
        re_path(r'^docs/(?P<path>.*)$', serve, {'document_root': os.path.join(settings.BASE_DIR, 'docs')}),
    ]
