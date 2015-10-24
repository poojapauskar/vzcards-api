from ticket.models import Ticket
from friends.models import Friends
from sync.models import Sync
from register.models import Register
from get_my_friends.serializers import Get_my_friendsSerializer
from rest_framework import generics
# from ticket.permissions import IsOwnerOrReadOnly
# from rest_framework import permissions
from django.shortcuts import get_object_or_404
from django.db.models import Count 






class Get_my_friendsList(generics.ListCreateAPIView):
 queryset = Ticket.objects.all()
 serializer_class = Get_my_friendsSerializer
 # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class Get_my_friendsDetail(generics.ListAPIView):
 serializer_class = Get_my_friendsSerializer

 def get_queryset(self):
  vz_id = self.kwargs['vz_id']
        
  #contacts= Friends.objects.filter(vz_id=vz_id).values('friends_vz_id')
        
        #vz_id= Register.objects.filter(phone=contacts).values('vz_id')
  #tickets = Ticket.objects.filter(vz_id__in=contacts)

  #detail=[]    
  def ValuesQuerySetToDict(vqs):
    return [item for item in vqs]

  import json
  friends_list=list(sync_contact.encode("utf8") for sync_contact in Sync.objects.filter(vz_id=vz_id).values_list('friends_vz_id',flat=True))


  #friends_list = json.dumps(friends_list)

  #friends_list = json.dumps(friends_list)
  #print friends_list.query      
  #friends_list = json.dumps(friends_list)
       
  #friends_list=list(friends_list)

  import operator
  from django.db.models import Q

  import datetime
  today = datetime.datetime.today()

  import sys
  #print >> sys.stderr, friends_list.query
  #friends_list = json.dumps(friends_list)
  friends_list=str(friends_list).replace('["','').replace('"]','').replace(',','').replace('[','').replace(']','').replace("'",'')


  print >> sys.stderr, friends_list

  friends_list= friends_list.split()




  #friends_list = json.dumps(friends_list)

  #print >> sys.stderr, friends_list



  objects= Register.objects.filter(vz_id__in=friends_list)

  print >> sys.stderr, objects.query
  print >> sys.stderr, objects
  #objects= Ticket.objects.filter(vz_id__in=['VZ1445062511', 'VZ1445062656', 'VZ1445613566', 'VZ1445613959'])
  #print objects.query
#VZ1445062511, VZ1445062656, VZ1445613566, VZ1445613959
  # import pdb; 
  # pdb.set_trace()

  




  #.filter(date_validity__gte=today)
  
  return objects


  # import os

  # LOGGING = {
  #   'version': 1,
  #   'disable_existing_loggers': False,
  #   'handlers': {
  #       'console': {
  #           'class': 'logging.StreamHandler',
  #       },
  #   },
  #   'loggers': {
  #       'django': {
  #           'handlers': ['console'],
  #           'level': os.getenv('DJANGO_LOG_LEVEL', 'INFO'),
  #       },
  #   },
  # }

  # import logging

  # # Get an instance of a logger
  # logger = logging.getLogger(__name__)

  # def my_view(request, arg1, arg):
   
  #   if bad_mojo:
  #       # Log an error message
  #       logger.error('Something went wrong!')

  # logger.debug(friends_vz_id)
  

       

from django.contrib.auth.models import User
from get_my_friends.serializers import UserSerializer
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
