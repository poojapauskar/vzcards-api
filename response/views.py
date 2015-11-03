from connect.models import Connect
from register.models import Register
from ticket_create.models import Ticket_create
from response.serializers import ResponseSerializer
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

  #vz_id = self.kwargs['vz_id']
     
  vz_id= Register.objects.filter(token_generated=access_token).values_list('vz_id',flat=True)[0]
  #tickets = Ticket.objects.filter(vz_id__in=contacts)
  print >> sys.stderr, vz_id
  
  obj=Register.objects.get(vz_id=vz_id)
  from django.http import JsonResponse
 
  objects=(Connect.objects.filter(phone_1=obj.phone) | Connect.objects.filter(phone_2=obj.phone))
  print >> sys.stderr, objects

  import json

  def date_handler(obj):
    return obj.isoformat() if hasattr(obj, 'isoformat') else obj

  fields = []
  for obj1 in objects:
     if(obj1.phone_1==obj.phone):
      fields.append(
              {
               'connecter_details':(json.dumps(list(Register.objects.filter(vz_id=obj1.connecter_vz_id).values_list('phone','photo','firstname', 'lastname', 'email','vz_id','industry','company','address_line_1','address_line_2','city','pin_code')))).replace('"','').replace('[','').replace(']',''), 
               'my_details':(json.dumps(list(Register.objects.filter(phone=obj1.phone_1).values_list('phone','photo','firstname', 'lastname', 'email','vz_id','industry','company','address_line_1','address_line_2','city','pin_code')))).replace('"','').replace('[','').replace(']',''),  
               'my_ticket':(json.dumps(list(Ticket_create.objects.filter(ticket_id=obj1.ticket_id_1).values_list('vz_id','item_photo', 'question', 'item', 'description','date_created', 'date_validity','ticket_id')), default=date_handler)).replace('"','').replace('[','').replace(']',''), 
               'reffered_to':(json.dumps(list(Register.objects.filter(phone=obj1.phone_2).values_list('phone','photo','firstname', 'lastname', 'email','vz_id','industry','company','address_line_1','address_line_2','city','pin_code')))).replace('"','').replace('[','').replace(']',''), 
               'reffered_ticket':(json.dumps(list(Ticket_create.objects.filter(ticket_id=obj1.ticket_id_2).values_list('vz_id','item_photo','question', 'item', 'description','date_created', 'date_validity','ticket_id')), default=date_handler)).replace('"','').replace('[','').replace(']',''), 
              }
            )
     else:
      fields.append(
              {
               'connecter_details':(json.dumps(list(Register.objects.filter(vz_id=obj1.connecter_vz_id).values_list('phone','photo','firstname', 'lastname', 'email','vz_id','industry','company','address_line_1','address_line_2','city','pin_code')))).replace('"','').replace('[','').replace(']',''), 
               'my_details':(json.dumps(list(Register.objects.filter(phone=obj1.phone_2).values_list('phone','photo','firstname', 'lastname', 'email','vz_id','industry','company','address_line_1','address_line_2','city','pin_code')))).replace('"','').replace('[','').replace(']',''), 
               'my_ticket':(json.dumps(list(Ticket_create.objects.filter(ticket_id=obj1.ticket_id_2).values_list('vz_id','item_photo','question', 'item', 'description','date_created', 'date_validity','ticket_id')), default=date_handler)).replace('"','').replace('[','').replace(']',''), 
               'reffered_to':(json.dumps(list(Register.objects.filter(phone=obj1.phone_1).values_list('phone','photo','firstname', 'lastname', 'email','vz_id','industry','company','address_line_1','address_line_2','city','pin_code')))).replace('"','').replace('[','').replace(']',''), 
               'reffered_ticket':(json.dumps(list(Ticket_create.objects.filter(ticket_id=obj1.ticket_id_1).values_list('vz_id','item_photo', 'question', 'item', 'description','date_created', 'date_validity','ticket_id')), default=date_handler)).replace('"','').replace('[','').replace(']',''), 
              }
            )
    
     print >> sys.stderr,"-----------"
     print >> sys.stderr,fields
     print >> sys.stderr,"-----------"

     

  return JsonResponse(list(fields),safe=False)



       

from django.contrib.auth.models import User
from response.serializers import UserSerializer
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
