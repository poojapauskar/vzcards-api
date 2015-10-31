from ticket_create.models import Ticket_create
from ticket_details.serializers import Ticket_detailsSerializer
from rest_framework import generics
# from ticket.permissions import IsOwnerOrReadOnly
# from rest_framework import permissions
from django.shortcuts import get_object_or_404


class Ticket_detailsDetail(generics.ListAPIView):
 serializer_class = Ticket_detailsSerializer

 def get_queryset(self):
  ticket_id = self.kwargs['ticket_id']

  objects=Ticket_create.objects.filter(ticket_id=ticket_id) 
  

  return objects


       

from django.contrib.auth.models import User
from ticket_details.serializers import UserSerializer
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
