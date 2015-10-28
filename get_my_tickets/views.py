from ticket.models import Ticket
from get_my_tickets.serializers import Get_my_ticketsSerializer
from rest_framework import generics
# from ticket.permissions import IsOwnerOrReadOnly
# from rest_framework import permissions
from django.shortcuts import get_object_or_404






# class Get_my_ticketsList(generics.ListCreateAPIView):
#  queryset = Ticket.objects.all()
#  serializer_class = Get_my_ticketsSerializer
#  # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)



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

def get_queryset(request):
  access_token = request.GET.get('access_token')
  import sys
  print >> sys.stderr, access_token

  #vz_id = self.kwargs['vz_id']
     
  vz_id= Register.objects.filter(token_generated=access_token).values_list('vz_id',flat=True)[0]
  #tickets = Ticket.objects.filter(vz_id__in=contacts)
  print >> sys.stderr, vz_id

  objects= Ticket.objects.filter(vz_id=vz_id).values('vz_id', 'question', 'item', 'description','date_created','date_validity','ticket_id')

  from django.http import JsonResponse
  #return JsonResponse(dict(objects=list(objects)))
  return JsonResponse((list(objects)),safe=False)

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




