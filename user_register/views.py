from user_register.models import User_register
from user_register.serializers import User_registerSerializer
from rest_framework import generics
# from user_register.permissions import IsOwnerOrReadOnly
# from rest_framework import permissions


class User_registerList(generics.ListCreateAPIView):
 queryset = User_register.objects.all()
 serializer_class = User_registerSerializer
 # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)



class User_registerDetail(generics.RetrieveUpdateDestroyAPIView):
 queryset = User_register.objects.all()
 serializer_class = User_registerSerializer
 # permission_classes = (permissions.IsAuthenticatedOrReadOnly,
 #                      IsOwnerOrReadOnly,)


from django.contrib.auth.models import User
from user_register.serializers import UserSerializer
from rest_framework import permissions


class UserList(generics.ListAPIView):
 queryset = User.objects.all()
 serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
 queryset = User.objects.all()
 serializer_class = UserSerializer


def perform_create(self, serializer):
 serializer.save(owner=self.request.user)

