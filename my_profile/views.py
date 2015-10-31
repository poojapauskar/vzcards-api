from register.models import Register
from my_profile.serializers import My_profileSerializer
from rest_framework import generics
# from ticket.permissions import IsOwnerOrReadOnly
# from rest_framework import permissions
from django.shortcuts import get_object_or_404

class My_profileList(generics.ListCreateAPIView):
 queryset = Register.objects.all()
 serializer_class = My_profileSerializer
 # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


def get_queryset(request):
  access_token = request.GET.get('access_token')
  import sys
  print >> sys.stderr, access_token

  #vz_id = self.kwargs['vz_id']
     
  vz_id= Register.objects.filter(token_generated=access_token).values_list('vz_id',flat=True)[0]
  #tickets = Ticket.objects.filter(vz_id__in=contacts)
  print >> sys.stderr, vz_id
  
  profile=Register.objects.filter(vz_id=vz_id).values('phone','photo','vz_id','firstname','lastname','email','industry','company','address_line_1','address_line_2','city','pin_code')

  from django.http import JsonResponse
  #return JsonResponse(dict(objects=list(objects)))
  return JsonResponse((list(profile)),safe=False)


       

from django.contrib.auth.models import User
from my_profile.serializers import UserSerializer
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
