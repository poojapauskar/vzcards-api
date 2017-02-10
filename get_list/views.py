from ticket_create.models import Ticket_create
from connect.models import Connect
from friends.models import Friends
from sync.models import Sync
from user_register.models import User_register
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

from django.views import generic
from django.views.generic import ListView

class CustomListView(ListView):
    #paginate_by = 2
    def get(self, request, *args, **kwargs):
      
      access_token = request.GET.get('access_token')

      import sys
      print >> sys.stderr, access_token

      error=[]

      if(User_register.objects.filter(token_generated=access_token).exists()):
        pass
      else:
        error.append(
                  {
                    'status':401,
                    'message':"Access Token not valid"
                  }
            )
        return JsonResponse(error[0],safe=False)



   

      #vz_id = self.kwargs['vz_id']
         
      vz_id= User_register.objects.filter(token_generated=access_token).values_list('vz_id',flat=True)[0]
      #tickets = Ticket.objects.filter(vz_id__in=contacts)
      print >> sys.stderr, vz_id

      is_organization=User_register.objects.filter(vz_id=vz_id).values_list('is_organization',flat=True)[0]
      print >> sys.stderr, is_organization

      if(is_organization=='true'):
       company= User_register.objects.filter(vz_id=vz_id).values_list('company',flat=True)[0]
       friends_list=list(User_register.objects.filter(company=company).values_list('vz_id',flat=True))
       print >> sys.stderr, "friends_list 1------------------------>"
       print >> sys.stderr, friends_list
       friends_list=str(friends_list).replace('u','').replace('["','').replace('"]','').replace(',','').replace('[','').replace(']','').replace("'",'')
       print >> sys.stderr, "friends_list 2------------------------>"
       print >> sys.stderr, friends_list
      else:
       friends_list=list(sync_contact.encode("utf8") for sync_contact in Sync.objects.filter(vz_id=vz_id).values_list('friends_vz_id',flat=True))
       print >> sys.stderr, "friends_list 1------------------------>"
       print >> sys.stderr, friends_list
       friends_list=str(friends_list).replace('["','').replace('"]','').replace(',','').replace('[','').replace(']','').replace("'",'')
       print >> sys.stderr, "friends_list 2------------------------>"
       print >> sys.stderr, friends_list
      

      import json
      
      import datetime
      today = datetime.datetime.today()
      

      print >> sys.stderr, "today"
      print >> sys.stderr, today



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

          if(Ticket_create.objects.filter(ticket_id=obj1.ticket_id).filter(date_validity__gte=today).exists()):
            fields.append(
                  { 
                   'feed':Ticket_create.objects.filter(ticket_id=obj1.ticket_id).filter(date_validity__gte=today).values('vz_id','item_photo','question', 'item', 'description','date_created','date_validity','ticket_id')[0],
                   'user_details':User_register.objects.filter(vz_id=obj1.vz_id).values('pk','token_generated','company_photo','company_photo','photo','firstname', 'lastname', 'title', 'email', 'phone','vz_id','industry','company','address_line_1','address_line_2','city','pin_code','otp_generated')[0],  
                   }
                )
          else :
            print >> sys.stderr, "0"
          #question=[]
          #feeds=[]
          #user_details=[]
          

          
          
          print >> sys.stderr,"-----------"
          print >> sys.stderr,fields
          print >> sys.stderr,"-----------"
          #return JsonResponse(dict(objects=list(objects)))


      fields = fields[::-1]
      
      response=[]
      count=len(fields)
      
      from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
      # paginator = Paginator(response, self.paginate_by)
      paginator = Paginator(fields, 10)

      page = self.request.GET.get('page')

      print >> sys.stderr,"-----page------"
      print >> sys.stderr,page
      

      try:
          fields = paginator.page(page)
      except PageNotAnInteger:
          fields = paginator.page(1)
      except EmptyPage:
          fields = paginator.page(paginator.num_pages)


      print >> sys.stderr,"-----fields------"
      print >> sys.stderr,fields

      response.append(
                  {
                    'count':count,
                    'response':list(fields)
                  }
            )
      
      

      # Connect.objects.all().delete()
      # Ticket_create.objects.all().delete() 
      # context['list_exams'] = file_exams
      #return files   
      #return JsonResponse(response[0],safe=False)
      return JsonResponse(response[0],safe=False)
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
