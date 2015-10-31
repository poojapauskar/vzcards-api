from connect.models import Connect
from register.models import Register
from ticket_create.models import Ticket_create
from response.serializers import ResponseSerializer
from rest_framework import generics
# from ticket.permissions import IsOwnerOrReadOnly
# from rest_framework import permissions
from django.shortcuts import get_object_or_404


def get_queryset(request):
  access_token = request.GET.get('access_token')
  import sys
  print >> sys.stderr, access_token

  #vz_id = self.kwargs['vz_id']
     
  vz_id= Register.objects.filter(token_generated=access_token).values_list('vz_id',flat=True)[0]
  #tickets = Ticket.objects.filter(vz_id__in=contacts)
  print >> sys.stderr, vz_id
  
  obj=Register.objects.get(vz_id=vz_id)

  #objects=(Connect.objects.filter(phone_1=obj.phone) | Connect.objects.filter(phone_2=obj.phone)).values('connecter_vz_id', 'phone_1', 'ticket_id_1', 'phone_2', 'ticket_id_2')
  
  # connecter_vz_id=(Connect.objects.filter(phone_1=obj.phone) | Connect.objects.filter(phone_2=obj.phone)).values('connecter_vz_id')
  # phone_1=(Connect.objects.filter(phone_1=obj.phone) | Connect.objects.filter(phone_2=obj.phone)).values('phone_1')
  # ticket_id_1=(Connect.objects.filter(phone_1=obj.phone) | Connect.objects.filter(phone_2=obj.phone)).values('ticket_id_1')
  # phone_2=(Connect.objects.filter(phone_1=obj.phone) | Connect.objects.filter(phone_2=obj.phone)).values('phone_2')
  # ticket_id_2=(Connect.objects.filter(phone_1=obj.phone) | Connect.objects.filter(phone_2=obj.phone)).values('ticket_id_2')

  # user_details=(Register.objects.filter(phone__in=phone_1) | Register.objects.filter(phone__in=phone_2) | Register.objects.filter(vz_id__in=connecter_vz_id)).values('phone','firstname', 'lastname', 'email','vz_id','industry','company','address_line_1','address_line_2','city','pin_code')
  # ticket_details=(Ticket.objects.filter(ticket_id=ticket_id_1) | Ticket.objects.filter(ticket_id=ticket_id_2)).values('vz_id','user_details', 'question', 'item', 'description','date_created','date_validity','ticket_id')




  from django.http import JsonResponse
  # from rest_framework.response import Response
  # #return JsonResponse(dict(objects=list(objects)))
  # #return JsonResponse((list(objects)),safe=False)
  
  
  # print >> sys.stderr, user_details
  # print >> sys.stderr, ticket_details
  
  # return Response({
  #  'user_details': user_details,
  #  'ticket_details': ticket_details,status=None, template_name=None, headers=None, content_type=None
  # })




  # from django.http import JsonResponse
  objects=(Connect.objects.filter(phone_1=obj.phone) | Connect.objects.filter(phone_2=obj.phone)).values('connecter_vz_id','connecter_details', 'phone_1', 'ticket_id_1', 'phone_2', 'ticket_id_2','ticket_1_details','ticket_2_details','phone_1_details','phone_2_details')
  print >> sys.stderr, objects

  return JsonResponse((list(objects)),safe=False)
  #return objects
  
  # import json
  # #from json import simplejson
  # from django.http import HttpResponse

  # json = json.dumps({'user_details': user_details, 'ticket_details': list(ticket_details), 'objects': list(objects)})
  # return JsonResponse((json),safe=False)
  # #return HttpResponse(json, mimetype='text/json')


       

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
