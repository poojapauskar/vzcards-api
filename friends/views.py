from friends.models import Friends
from friends.serializers import FriendsSerializer
from rest_framework import generics
# from friends.permissions import IsOwnerOrReadOnly
# from rest_framework import permissions





class FriendsList(generics.ListCreateAPIView):
 queryset = Friends.objects.all()
 serializer_class = FriendsSerializer
 # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)



class FriendsDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Friends.objects.all()
  serializer_class = FriendsSerializer
  # permission_classes = (permissions.IsAuthenticatedOrReadOnly,
  #                     IsOwnerOrReadOnly,)


class FriendsDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Friends.objects.all()
  serializer_class = FriendsSerializer
  # permission_classes = (permissions.IsAuthenticatedOrReadOnly,
  #                     IsOwnerOrReadOnly,)
  
        #do something with this user


from django.contrib.auth.models import User
from friends.serializers import UserSerializer
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
