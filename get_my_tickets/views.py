from ticket.models import Ticket
from get_my_tickets.serializers import Get_my_ticketsSerializer
from rest_framework import generics
# from ticket.permissions import IsOwnerOrReadOnly
# from rest_framework import permissions
from django.shortcuts import get_object_or_404






class Get_my_ticketsList(generics.ListCreateAPIView):
 queryset = Ticket.objects.all()
 serializer_class = Get_my_ticketsSerializer
 # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)



#class Get_listDetail(generics.ListCreateAPIView):
  #def get_queryset(self):
        #self.vz_id = get_object_or_404(Create, vz_id=self.args)
        # serializer_class = Get_listSerializer
        # return Create.objects.filter(vz_id=self.vz_id)
        #lookup_field = self.vz_id
        # queryset = Create.objects.filter(vz_id=lookup_field)
        # serializer_class = Get_listSerializer
        # permission_classes = (permissions.IsAuthenticatedOrReadOnly,
        #               IsOwnerOrReadOnly,)
  
        #do something with this user

class Get_my_ticketsDetail(generics.ListAPIView):
    serializer_class = Get_my_ticketsSerializer

    def get_queryset(self):
        vz_id = self.kwargs['vz_id']
        return Ticket.objects.filter(vz_id=vz_id)

from django.contrib.auth.models import User
from get_list.serializers import UserSerializer
from rest_framework import permissions


class UserList(generics.ListAPIView):
 queryset = User.objects.all()
 serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
 queryset = User.objects.all()
 serializer_class = UserSerializer


def perform_create(self, serializer):
 serializer.save(owner=self.request.user)




