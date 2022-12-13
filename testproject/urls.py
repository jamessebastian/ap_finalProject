"""testproject URL Configuration

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
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('base.urls')),
    path('firstpage', views.test_page),
    path('test', views.render_page),
    path('index', views.index_page),

    path('login2', views.login_page),
    path('register2', views.register_page),

    path('', views.rooms_page),
    path('book_room', views.book_room_page),
    path('your_bookings', views.your_bookings_page),

    path('admin_user', views.admin_user_page),
    path('admin_edit_user', views.admin_edit_user_page),
    path('admin_add_user', views.admin_add_user_page),

    path('admin_rooms', views.admin_rooms_page),
    path('admin_edit_rooms', views.admin_edit_rooms_page),
    path('admin_add_rooms', views.admin_add_rooms_page),

    path('admin_bookings', views.admin_bookings_page),
    path('admin_edit_bookings', views.admin_edit_bookings_page),
    path('admin_add_bookings', views.admin_add_rooms_page),

    path('admin_services', views.admin_services_page),
    path('admin_edit_services', views.admin_edit_services_page),
    path('admin_add_services', views.admin_add_services_page),


]
