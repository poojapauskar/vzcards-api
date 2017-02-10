from ticket_create.models import Ticket_create
from register.models import Register
from get_my_tickets.serializers import Get_my_ticketsSerializer
from rest_framework import generics
# from ticket.permissions import IsOwnerOrReadOnly
# from rest_framework import permissions
from django.shortcuts import get_object_or_404



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

def get_queryset(request):
  access_token = request.GET.get('access_token')
  if(Register.objects.filter(token_generated=access_token).exists()):
    pass
  else:
    return JSONResponse(status = StatusCode.NOT_FOUND)

    
  import sys
  print >> sys.stderr, access_token

  # valid="Access token not valid"
  # from django.http import JsonResponse

  # if(Register.objects.filter(token_generated=access_token).exists()):
  #   pass
  # else:
  #   return JsonResponse(valid,safe=False)

  #vz_id = self.kwargs['vz_id']
     
  vz_id= Register.objects.filter(token_generated=access_token).values_list('vz_id',flat=True)[0]
  #tickets = Ticket.objects.filter(vz_id__in=contacts)
  print >> sys.stderr, vz_id

  objects= Ticket_create.objects.filter(vz_id=vz_id)
  

  my_tickets=[]

  for obj1 in objects:
    my_tickets.append(
                {
                  'vz_id':Ticket_create.objects.filter(vz_id=obj1.ticket_id).values_list('vz_id'), 
                  'question':Ticket_create.objects.filter(vz_id=obj1.ticket_id).values_list('question'), 
                  'item':Ticket_create.objects.filter(vz_id=obj1.ticket_id).values_list('item'),  
                  'description':Ticket_create.objects.filter(vz_id=obj1.ticket_id).values_list('description'), 
                  'date_created':Ticket_create.objects.filter(vz_id=obj1.ticket_id).values_list('date_created'), 
                  'date_validity':Ticket_create.objects.filter(vz_id=obj1.ticket_id).values_list('date_validity'), 
                  'ticket_id':Ticket_create.objects.filter(vz_id=obj1.ticket_id).values_list('ticket_id')
                }
              )

  

  from django.http import JsonResponse
  #return JsonResponse(dict(objects=list(objects)))
  return JsonResponse((list(my_tickets)),safe=False)

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




