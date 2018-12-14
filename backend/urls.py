"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
"""

from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from .api.views import index_view
from .api.views import UserViewSet

UserViewSet.as_view({
    'get': 'get'
})

router = routers.DefaultRouter()
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [

    # http://localhost:8000/
    path('', index_view, name='index'),

    # http://localhost:8000/api/<router-viewsets>
    path('api/', include(router.urls)),

    # http://localhost:8000/admin/
    path('admin/', admin.site.urls),
]
