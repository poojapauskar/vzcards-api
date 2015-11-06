from connect.models import Connect
from register.models import Register
from ticket_create.models import Ticket_create
from history.serializers import HistorySerializer
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
  
  obj=Ticket_create.objects.filter(vz_id=vz_id)
  from django.http import JsonResponse
 
  # objects=Connect.objects.filter(my_ticket__in=obj) 
  # print >> sys.stderr, objects

  print >> sys.stderr,"obj"
  print >> sys.stderr,obj

  import json

  def date_handler(obj):
    return obj.isoformat() if hasattr(obj, 'isoformat') else obj

  fields = []
  connections=[]

  for t in obj:
    print >> sys.stderr,t.ticket_id
    connect=Connect.objects.filter(my_ticket=t.ticket_id)
    print >> sys.stderr,"connect"
    print >> sys.stderr,connect

    for c in connect:
      connections.append(
                {
                 'connecter_details':(json.dumps(list(Register.objects.filter(vz_id=c.connecter_vz_id).values('phone','photo','firstname', 'lastname', 'email','vz_id','industry','company','address_line_1','address_line_2','city','pin_code')), default=date_handler)).replace('"','').replace('[','').replace(']',''), 
                 'reffered_details':(json.dumps(list(Register.objects.filter(phone=c.reffered_phone).values('phone','photo','firstname', 'lastname', 'email','vz_id','industry','company','address_line_1','address_line_2','city','pin_code')), default=date_handler)).replace('"','').replace('[','').replace(']',''), 
                 'reffered_ticket':(json.dumps(list(Ticket_create.objects.filter(ticket_id=c.reffered_ticket).values('vz_id','item_photo', 'question', 'item', 'description','date_created', 'date_validity','ticket_id')), default=date_handler)).replace('"','').replace('[','').replace(']',''), 
                               
                }
              )
    print >> sys.stderr,"connections"
    print >> sys.stderr,connections

    fields.append(
                {
                 'ticket_details':(json.dumps(list(Ticket_create.objects.filter(ticket_id=t.ticket_id).values('vz_id','item_photo', 'question', 'item', 'description','date_created', 'date_validity','ticket_id')), default=date_handler)).replace('"','').replace('[','').replace(']',''), 
                 'connections':connections
                }
              )


  print >> sys.stderr,"-----------"
  print >> sys.stderr,fields
  print >> sys.stderr,"-----------"

     

  return JsonResponse(list(fields),safe=False)


       

from django.contrib.auth.models import User
from history.serializers import UserSerializer
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
