from sync.models import Sync
from sync.serializers import SyncSerializer
from rest_framework import generics
# from sync.permissions import IsOwnerOrReadOnly
# from rest_framework import permissions





class SyncList(generics.ListCreateAPIView):
 queryset = Sync.objects.all()
 serializer_class = SyncSerializer
 # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)



class SyncDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Sync.objects.all()
  serializer_class = SyncSerializer
  # permission_classes = (permissions.IsAuthenticatedOrReadOnly,
  #                     IsOwnerOrReadOnly,)


class SyncDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Sync.objects.all()
  serializer_class = SyncSerializer
  # permission_classes = (permissions.IsAuthenticatedOrReadOnly,
  #                     IsOwnerOrReadOnly,)
  
        #do something with this user


from django.contrib.auth.models import User
from sync.serializers import UserSerializer
from rest_framework import permissions


class UserList(generics.ListAPIView):
 queryset = User.objects.all()
 serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
 queryset = User.objects.all()
 serializer_class = UserSerializer


def perform_create(self, serializer):
 serializer.save(owner=self.request.user)




from django.shortcuts import render

# Create your views here.
