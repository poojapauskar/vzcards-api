from ticket_create.models import Ticket_create
from friends.models import Friends
from sync.models import Sync
from user_register.models import User_register
from get_my_friends.serializers import Get_my_friendsSerializer
from rest_framework import generics
# from ticket.permissions import IsOwnerOrReadOnly
# from rest_framework import permissions
from django.shortcuts import get_object_or_404
from django.db.models import Count 


from django.http import JsonResponse

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
    def get(self, request, *args, **kwargs):
      access_token = request.GET.get('access_token')

      from django.http import JsonResponse
      
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

      import sys
      print >> sys.stderr, access_token

      valid="Access token not valid"
      from django.http import JsonResponse
 
      #vz_id = self.kwargs['vz_id']
         
      company= User_register.objects.filter(token_generated=access_token).values_list('company',flat=True)[0]
      #tickets = Ticket.objects.filter(vz_id__in=contacts)
      print >> sys.stderr, company

       
      my_friends=[] 

      objects=User_register.objects.filter(company=company).values('vz_id')
      
      
      fields=User_register.objects.filter(vz_id__in=objects).values('firstname','lastname','title','email','company_photo','phone','industry','company','address_line_1','address_line_2','city','pin_code','photo').order_by('firstname','lastname')
      count=len(fields)

      # fields = fields[::-1]

      from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
      # paginator = Paginator(response, self.paginate_by)
      paginator = Paginator(fields, 20)

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


      my_friends.append(
                    {
                         'count':count,
                         'response':list(fields), 
                    }
                   )

      

       
      #return JsonResponse(dict(objects=list(objects)))
      return JsonResponse(my_friends[0],safe=False)



  #.filter(date_validity__gte=today)
  
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
