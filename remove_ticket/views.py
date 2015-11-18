from ticket_create.models import Ticket_create
from connect.models import Connect
from remove_ticket.serializers import Remove_ticketSerializer
from rest_framework import generics
# from ticket.permissions import IsOwnerOrReadOnly
# from rest_framework import permissions
from django.shortcuts import get_object_or_404

from django.http import JsonResponse



class Remove_ticketDetail(generics.ListAPIView):
 serializer_class = Remove_ticketSerializer


 def get_queryset(self):
  ticket_id = self.kwargs['ticket_id']

  objects1=Ticket_create.objects.filter(ticket_id=ticket_id)
 
  objects=Ticket_create.objects.filter(ticket_id=ticket_id).delete()
  objects3=(Connect.objects.filter(ticket_id_1=ticket_id)|Connect.objects.filter(ticket_id_2=ticket_id)).delete()

  
  return objects1


       

from django.contrib.auth.models import User
from remove_ticket.serializers import UserSerializer
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
