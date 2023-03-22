"""settings URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include

from blog.views import main_page, blog_page

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('blog/', include('blog.urls')),
    path('', main_page),
    path("post/<slug:post_slug>/", blog_page, name="post"),
    path("postad", blog_page),
    path('home', main_page, name='home'),
    path('blog', include('blog.urls')),

]
