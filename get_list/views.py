from ticket_create.models import Ticket_create
from friends.models import Friends
from sync.models import Sync
from register.models import Register
from get_list.serializers import Get_listSerializer
from rest_framework import generics
# from ticket.permissions import IsOwnerOrReadOnly
# from rest_framework import permissions
from django.shortcuts import get_object_or_404
from django.db.models import Count 
from django.http import JsonResponse

# class Get_listList(generics.ListCreateAPIView):
#  queryset = Ticket.objects.all()
#  serializer_class = Get_listSerializer
 # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class StatusCode(object):
    OK = 200
    NOT_FOUND = 404
    # add more status code according to your need
import json
from django.http import HttpResponse
 
def JSONResponse(data = None, status = StatusCode.OK):
    if data is None:
        return HttpResponse(status)
    if data and type(data) is dict:
        return HttpResponse(json.dumps(data, indent = 4, encoding = 'utf-8', sort_keys = True), \
            mimetype = 'application/json', status = status)
    else:
        return HttpResponse(status = StatusCode.NOT_FOUND)



def get_queryset(request):
  access_token = request.GET.get('access_token')
  if(Register.objects.filter(token_generated=access_token).exists()):
    pass
  else:
    return JSONResponse(status = StatusCode.NOT_FOUND)



  import sys
  print >> sys.stderr, access_token

  #vz_id = self.kwargs['vz_id']
     
  vz_id= Register.objects.filter(token_generated=access_token).values_list('vz_id',flat=True)[0]
  #tickets = Ticket.objects.filter(vz_id__in=contacts)
  print >> sys.stderr, vz_id

  import json
  friends_list=list(sync_contact.encode("utf8") for sync_contact in Sync.objects.filter(vz_id=vz_id).values_list('friends_vz_id',flat=True))


  import datetime
  today = datetime.datetime.today()
  friends_list=str(friends_list).replace('["','').replace('"]','').replace(',','').replace('[','').replace(']','').replace("'",'')


  print >> sys.stderr, friends_list

  friends_list= friends_list.split()

  if(friends_list==''):
   objects=''
  else:
   objects=Ticket_create.objects.filter(vz_id__in=friends_list)

  #print >> sys.stderr, objects.query
  print >> sys.stderr, objects
 
  from django.http import HttpResponse
  #return HttpResponse(objects,content_type='application/json')

  def date_handler(obj):
    return obj.isoformat() if hasattr(obj, 'isoformat') else obj

  fields = []
  for obj1 in objects:
      question=[]
      feeds=[]
      user_details=[]
      fields.append(
              {
               'question':list(Ticket_create.objects.filter(ticket_id=obj1.ticket_id).filter(date_validity__gte=today).values('question')), 
               'feeds':list(Ticket_create.objects.filter(ticket_id=obj1.ticket_id).filter(date_validity__gte=today).values('vz_id','item_photo','question', 'item', 'description','date_created','date_validity','ticket_id')),
               'user_details':list(Register.objects.filter(vz_id=obj1.vz_id).values('pk','token_generated','photo','firstname', 'lastname', 'email', 'phone','vz_id','industry','company','address_line_1','address_line_2','city','pin_code','otp_generated')),  
               }
            )
    
      print >> sys.stderr,"-----------"
      print >> sys.stderr,fields
      print >> sys.stderr,"-----------"
      #return JsonResponse(dict(objects=list(objects)))
      
  return JsonResponse((list(fields)),safe=False)
  #return objects


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
