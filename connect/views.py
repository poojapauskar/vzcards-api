from connect.models import Connect
from connect.serializers import ConnectSerializer
from rest_framework import generics
# from connect.permissions import IsOwnerOrReadOnly
# from rest_framework import permissions


class ConnectList(generics.ListCreateAPIView):
 queryset = Connect.objects.all()
 serializer_class = ConnectSerializer
 # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)



class ConnectDetail(generics.RetrieveUpdateDestroyAPIView):
 queryset = Connect.objects.all()
 serializer_class = ConnectSerializer
 # permission_classes = (permissions.IsAuthenticatedOrReadOnly,
 #                      IsOwnerOrReadOnly,)


from django.contrib.auth.models import User
from connect.serializers import UserSerializer
from rest_framework import permissions


class UserList(generics.ListAPIView):
 queryset = User.objects.all()
 serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
 queryset = User.objects.all()
 serializer_class = UserSerializer


def perform_create(self, serializer):
 serializer.save(owner=self.request.user)




