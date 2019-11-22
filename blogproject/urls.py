"""blogproject URL Configuration

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
from django.urls import path
from django.conf.urls import url, include
from blogapp import views as v1

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',v1.post_list_view),
    path('detail/<int:pk>',v1.BlogDetailView.as_view()),
    path('signup/',v1.signup_view),
    path('accounts/',include('django.contrib.auth.urls')),
    path('logout/',v1.logout_view),
    path('dashboard/',v1.dashboard_view),
    path('dashboard/<int:pk>/update',v1.update_view),
    path('dashboard/<int:pk>/delete',v1.delete_view),
    path('create/',v1.createview),
]
