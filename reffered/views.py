from connect.models import Connect
from register.models import Register
from reffered.serializers import RefferedSerializer
from rest_framework import generics
# from ticket.permissions import IsOwnerOrReadOnly
# from rest_framework import permissions
from django.shortcuts import get_object_or_404


class RefferedDetail(generics.ListAPIView):
 serializer_class = RefferedSerializer

 def get_queryset(self):
  vz_id = self.kwargs['vz_id']
  
  #obj=Register.objects.get(vz_id=vz_id)

  objects=Connect.objects.filter(connecter_vz_id=vz_id) 
  

  return objects


       

from django.contrib.auth.models import User
from reffered.serializers import UserSerializer
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
