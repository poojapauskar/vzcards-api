from ticket.models import Ticket
from ticket.serializers import TicketSerializer
from rest_framework import generics
# from ticket.permissions import IsOwnerOrReadOnly
# from rest_framework import permissions


class TicketList(generics.ListCreateAPIView):
 queryset = Ticket.objects.all()
 serializer_class = TicketSerializer
 # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)



class TicketDetail(generics.RetrieveUpdateDestroyAPIView):
 queryset = Ticket.objects.all()
 serializer_class = TicketSerializer
 # permission_classes = (permissions.IsAuthenticatedOrReadOnly,
 #                      IsOwnerOrReadOnly,)


from django.contrib.auth.models import User
from ticket.serializers import UserSerializer
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
