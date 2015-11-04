from create_ticket.models import Create_ticket
from create_ticket.serializers import Create_ticketSerializer
from rest_framework import generics
# from ticket.permissions import IsOwnerOrReadOnly
# from rest_framework import permissions


class Create_ticketList(generics.ListCreateAPIView):
 queryset = Create_ticket.objects.all()
 serializer_class = Create_ticketSerializer
 # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)



class Create_ticketDetail(generics.RetrieveUpdateDestroyAPIView):
 queryset = Create_ticket.objects.all()
 serializer_class = Create_ticketSerializer
 # permission_classes = (permissions.IsAuthenticatedOrReadOnly,
 #                      IsOwnerOrReadOnly,)


from django.contrib.auth.models import User
from create_ticket.serializers import UserSerializer
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
