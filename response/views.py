from connect.models import Connect
from register.models import Register
from response.serializers import ResponseSerializer
from rest_framework import generics
# from ticket.permissions import IsOwnerOrReadOnly
# from rest_framework import permissions
from django.shortcuts import get_object_or_404


class ResponseDetail(generics.ListAPIView):
 serializer_class = ResponseSerializer

 def get_queryset(self):
  vz_id = self.kwargs['vz_id']
  
  obj=Register.objects.get(vz_id=vz_id)

  objects=Connect.objects.filter(phone_1=obj.phone) | Connect.objects.filter(phone_2=obj.phone)
  

  return objects


       

from django.contrib.auth.models import User
from response.serializers import UserSerializer
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
