from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django.views.decorators.cache import never_cache

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer
from rest_framework.renderers import JSONRenderer

# Serve Vue Application
index_view = never_cache(TemplateView.as_view(template_name='index.html'))


class UserViewSet(viewsets.ViewSet):
    def list(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def create(self, request, format='json'):
        data = JSONRenderer().render(request.data)
        print(data)
        serializer = UserSerializer(data=data)
        serializer.create(request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        return Response(pk)

    def partial_update(self, request, pk=None):
        Response(request)

    def destroy(self, request, pk=None):
        Response(request)
