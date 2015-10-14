from ticket.models import Ticket
from friends.models import Friends
from register.models import Register
from get_list.serializers import Get_listSerializer
from rest_framework import generics
# from ticket.permissions import IsOwnerOrReadOnly
# from rest_framework import permissions
from django.shortcuts import get_object_or_404






class Get_listList(generics.ListCreateAPIView):
 queryset = Ticket.objects.all()
 serializer_class = Get_listSerializer
 # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class Get_listDetail(generics.ListAPIView):
 serializer_class = Get_listSerializer

 def get_queryset(self):
  vz_id = self.kwargs['vz_id']
        
  contacts= Friends.objects.filter(vz_id=vz_id).values('contacts')
        
        #vz_id= Register.objects.filter(phone=contacts).values('vz_id')
        #tickets = Ticket.objects.filter(vz_id=vz_id)

  #detail=[]    

  phone_list = Friends.objects.filter(vz_id=vz_id).values('contacts')
  # for friend in friends:
  #  detail = Register.objects.filter(phone=friends).values('vz_id')
 	

  
  vz_id_list= Register.objects.filter(phone__in=phone_list).values('vz_id')       

  tickets = Ticket.objects.filter(vz_id__in=vz_id_list)

  return tickets
       

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




from django.shortcuts import render

# Create your views here.
