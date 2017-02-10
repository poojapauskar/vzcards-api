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
         
      vz_id= User_register.objects.filter(token_generated=access_token).values_list('vz_id',flat=True)[0]
      #tickets = Ticket.objects.filter(vz_id__in=contacts)
      print >> sys.stderr, vz_id
      def ValuesQuerySetToDict(vqs):
        return [item for item in vqs]

      is_organization=User_register.objects.filter(vz_id=vz_id).values_list('is_organization',flat=True)[0]
      if(is_organization=='true'):
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
      # from connect.models import Connect
      # Connect.objects.filter(connecter_vz_id="vz123").delete()

      #objects= Register.objects.filter(vz_id__in=friends_list).values('firstname', 'lastname', 'email', 'phone','vz_id','industry','company','address_line_1','address_line_2','city','pin_code','photo')
      def date_handler(obj):
        return obj.isoformat() if hasattr(obj, 'isoformat') else obj
      
      from django.http import JsonResponse  
      my_friends=[]

      if(friends_list==''):
       return JsonResponse((list(my_friends)),safe=False)
      else:
       # objects=Register.objects.filter(vz_id__in=friends_list)
       # for obj1 in objects:
       #  my_friends.append(
       #              {
       #                list(Register.objects.filter(vz_id=obj1.vz_id).values('firstname','lastname','email','phone','industry','company','address_line_1','address_line_2','city','pin_code','photo')), 
       #              }
       #            )

       objects=User_register.objects.filter(vz_id__in=friends_list).values('vz_id')
      
       
       


      #print >> sys.stderr, objects.query
       #print >> sys.stderr, my_friends
      #objects= Ticket.objects.filter(vz_id__in=['VZ1445062511', 'VZ1445062656', 'VZ1445613566', 'VZ1445613959'])
      #print objects.query
    #VZ1445062511, VZ1445062656, VZ1445613566, VZ1445613959
      # import pdb; 
      # pdb.set_trace()
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
