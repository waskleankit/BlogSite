"""BlogSite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from BlogSite.views import  home, about, dashboard ,createblog ,post_detail ,edit, post_user ,deletepost ,update,home2
from BlogSite.views import dashboard2 , selectedplan ,thank
from django.urls import include
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('home/', home),
    path('about/', about),
    path('dashboard/', dashboard,name='dashboard'),
    path('createblog/', createblog),
    path('<int:post_id>/', post_detail,name='post_detail'),
    path('blogadmin/',include("BlogAdmin.urls")),
    path('edit/<int:post_id>/', edit,name='edit'),
    path('post_user', post_user),
    path('deletepost', deletepost),
    path('update', update),
    path('home2/<int:category_id>/', home2),
    path('dashboard2/<int:category_id>/', dashboard2),
    path('accounts/', include('allauth.urls')),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('selectedplan/', selectedplan),
    path('thank/', thank,name="thank"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
