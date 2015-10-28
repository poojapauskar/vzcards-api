from connect.models import Connect
from register.models import Register
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

  objects=(Connect.objects.filter(phone_1=obj.phone) | Connect.objects.filter(phone_2=obj.phone)).values('connecter_vz_id', 'phone_1', 'ticket_id_1', 'phone_2', 'ticket_id_2')
  
  from django.http import JsonResponse
  #return JsonResponse(dict(objects=list(objects)))
  return JsonResponse((list(objects)),safe=False)

  #return objects


       

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
