"""
URL configuration for myproject project.

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
from django.urls import path
from myapp.views import index_page, time_page, calc_page, home, expression, history, delete_last_expression

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_page, name='index'),
    path('time/', time_page, name='time'),
    path('calc/', calc_page, name='calc'),
    path('', home, name='home'),
    path('expression/', expression, name='expression'),
    path('history/', history, name='history'),
    path('delete/', delete_last_expression, name='delete_last_expression'),
]