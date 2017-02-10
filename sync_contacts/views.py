from sync_contacts.models import Sync_contacts
from sync_contacts.serializers import Sync_contactsSerializer
from rest_framework import generics
# from sync_contacts.permissions import IsOwnerOrReadOnly
# from rest_framework import permissions





class Sync_contactsList(generics.ListCreateAPIView):
 queryset = Sync_contacts.objects.all()
 serializer_class = Sync_contactsSerializer
 # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)



class Sync_contactsDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Sync_contacts.objects.all()
  serializer_class = Sync_contactsSerializer
  # permission_classes = (permissions.IsAuthenticatedOrReadOnly,
  #                     IsOwnerOrReadOnly,)


class Sync_contactsDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Sync_contacts.objects.all()
  serializer_class = Sync_contactsSerializer
  # permission_classes = (permissions.IsAuthenticatedOrReadOnly,
  #                     IsOwnerOrReadOnly,)
  
        #do something with this user


from django.contrib.auth.models import User
from sync_contacts.serializers import UserSerializer
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
