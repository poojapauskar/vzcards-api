from api.models import Api
from api.serializers import ApiSerializer
from rest_framework import generics
# from api.permissions import IsOwnerOrReadOnly
# from rest_framework import permissions


class ApiList(generics.ListCreateAPIView):
 queryset = Api.objects.all()
 serializer_class = ApiSerializer
 # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)



class ApiDetail(generics.RetrieveUpdateDestroyAPIView):
 queryset = Api.objects.all()
 serializer_class = ApiSerializer
 # permission_classes = (permissions.IsAuthenticatedOrReadOnly,
 #                      IsOwnerOrReadOnly,)


from django.contrib.auth.models import User
from api.serializers import UserSerializer
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
