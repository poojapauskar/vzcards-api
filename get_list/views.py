from ticket.models import Ticket
from friends.models import Friends
from sync_contacts.models import Sync_contacts
from register.models import Register
from get_list.serializers import Get_listSerializer
from rest_framework import generics
# from ticket.permissions import IsOwnerOrReadOnly
# from rest_framework import permissions
from django.shortcuts import get_object_or_404
from django.db.models import Count 






class Get_listList(generics.ListCreateAPIView):
 queryset = Ticket.objects.all()
 serializer_class = Get_listSerializer
 # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class Get_listDetail(generics.ListAPIView):
 serializer_class = Get_listSerializer

 def get_queryset(self):
  vz_id = self.kwargs['vz_id']
        
  #contacts= Friends.objects.filter(vz_id=vz_id).values('friends_vz_id')
        
        #vz_id= Register.objects.filter(phone=contacts).values('vz_id')
  #tickets = Ticket.objects.filter(vz_id__in=contacts)

  #detail=[]    
  def ValuesQuerySetToDict(vqs):
    return [item for item in vqs]

  friends_vz_id = Sync_contacts.objects.filter(vz_id=vz_id).values('friends_vz_id')

  # import datetime
  # today = datetime.datetime.today()
  # tickets = Ticket.objects.filter(vz_id__in=friends_vz_id).filter(date_validity__gte=today)


   #endfor
  # endfor
  # import json, ast

  data_dict = ValuesQuerySetToDict(friends_vz_id)

  # from django.db.models import Q
  # filter_list = Q()
  # for item in friends_vz_id:
  #  filter_list |= Q(item)
   
  # tickets = Ticket.objects.filter(filter_list)

  # [d['vz_id'] for d in data_dict]

  # for element in data_dict: 
  #   print element
    # <input type="checkbox" name = "bar" value = "{{ value }}">{{ value }}<br>
    # objects=Sync_contacts.objects.create(vz_id=validated_data.get('vz_id'),contact_list=validated_data.get('contact_list'),friends_vz_id=value)
 

  # for element in data_dict: 
  #   return element
  #  objects=Ticket.objects.filter(vz_id=element)
  #  #print element.items
         
  #endfor 
  
  return data_dict
       

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
