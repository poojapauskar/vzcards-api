from upload_image.models import Upload_image
from connect.models import Connect
from ticket_create.models import Ticket_create
from friends.models import Friends
from sync.models import Sync
from user_register.models import User_register
from verify.models import Verify
from vzcard_details.serializers import Vzcard_detailsSerializer
from rest_framework import generics
# from ticket.permissions import IsOwnerOrReadOnly
# from rest_framework import permissions
from django.shortcuts import get_object_or_404
from django.db.models import Count 
from django.http import JsonResponse

# class Vzcard_detailsList(generics.ListCreateAPIView):
#  queryset = Ticket.objects.all()
#  serializer_class = Vzcard_detailsSerializer
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
      import sys
      # print >> sys.stderr, access_token

      import json
     
      from django.http import HttpResponse
      #return HttpResponse(objects,content_type='application/json')

      # count= len(Verify.objects.filter(valid='1'))
      # latest_valid_user=Verify.objects.filter(valid=1).values_list('phone',flat=True).order_by('-id')[0]
      # print >> sys.stderr, latest_valid_user

      # fields = []

      # fields.append(
      #         { 
      #          'count':count,
      #          'latest_user':list(User_register.objects.filter(phone=latest_valid_user).values('pk','token_generated','company_photo','photo','firstname', 'lastname', 'email', 'phone','vz_id','industry','company','address_line_1','address_line_2','city','pin_code','otp_generated'))
      #          }
      #       )
  
      from django.db.models import Q
      valid_users_count= len(User_register.objects.all().filter(~Q(token_generated = '')))
      number_of_posts= len(Ticket_create.objects.all())
      connections= len(Connect.objects.all())/2
      images_uploaded= len(Upload_image.objects.all())
      print >> sys.stderr, valid_users_count

      fields = []

      fields.append(
              { 
               'valid_users_count':valid_users_count,
               'number_of_posts':number_of_posts,
               'connections':connections,
               'images_uploaded':images_uploaded,
              }
            )

      return JsonResponse(list(fields),safe=False)
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
from vzcard_details.serializers import UserSerializer
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
