from ticket_create.models import Ticket_create
from ticket_create.serializers import Ticket_createSerializer
from rest_framework import generics
# from ticket_create.permissions import IsOwnerOrReadOnly
# from rest_framework import permissions


class Ticket_createList(generics.ListCreateAPIView):
 queryset = Ticket_create.objects.all()
 serializer_class = Ticket_createSerializer
 # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)



class Ticket_createDetail(generics.RetrieveUpdateDestroyAPIView):
 queryset = Ticket_create.objects.all()
 serializer_class = Ticket_createSerializer
 # permission_classes = (permissions.IsAuthenticatedOrReadOnly,
 #                      IsOwnerOrReadOnly,)


from django.contrib.auth.models import User
from ticket_create.serializers import UserSerializer
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
