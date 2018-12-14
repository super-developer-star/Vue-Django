from django.views.generic import TemplateView
from django.views.decorators.cache import never_cache

from rest_framework import viewsets
from rest_framework.response import Response

# Serve Vue Application
index_view = never_cache(TemplateView.as_view(template_name='index.html'))


class UserViewSet(viewsets.ViewSet):
    def list(self, request):
        Response(request)

    def create(self, request):
        Response(request)

    def retrieve(self, request, pk=None):
        Response(request)

    def update(self, request, pk=None):
        Response(request)

    def partial_update(self, request, pk=None):
        Response(request)

    def destroy(self, request, pk=None):
        Response(request)
