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
  
  
  profile=[]
  profile.append(
           {
            'phone':(json.dumps(list(Register.objects.filter(vz_id=vz_id).values_list('phone')))).replace('"','').replace('[','').replace(']',''),  
            'photo':(json.dumps(list(Register.objects.filter(vz_id=vz_id).values_list('photo')))).replace('"','').replace('[','').replace(']',''),  
            'firstname':(json.dumps(list(Register.objects.filter(vz_id=vz_id).values_list('firstname')))).replace('"','').replace('[','').replace(']',''),   
            'lastname':(json.dumps(list(Register.objects.filter(vz_id=vz_id).values_list('lastname')))).replace('"','').replace('[','').replace(']',''),  
            'email':(json.dumps(list(Register.objects.filter(vz_id=vz_id).values_list('email')))).replace('"','').replace('[','').replace(']',''),  
            'vz_id':(json.dumps(list(Register.objects.filter(vz_id=vz_id).values_list('vz_id')))).replace('"','').replace('[','').replace(']',''),  
            'industry':(json.dumps(list(Register.objects.filter(vz_id=vz_id).values_list('industry')))).replace('"','').replace('[','').replace(']',''),  
            'company':(json.dumps(list(Register.objects.filter(vz_id=vz_id).values_list('company')))).replace('"','').replace('[','').replace(']',''),  
            'address_line_1':(json.dumps(list(Register.objects.filter(vz_id=vz_id).values_list('address_line_1')))).replace('"','').replace('[','').replace(']',''),  
            'address_line_2':(json.dumps(list(Register.objects.filter(vz_id=vz_id).values_list('address_line_2')))).replace('"','').replace('[','').replace(']',''),  
            'city':(json.dumps(list(Register.objects.filter(vz_id=vz_id).values_list('city')))).replace('"','').replace('[','').replace(']',''),  
            'pin_code':(json.dumps(list(Register.objects.filter(vz_id=vz_id).values_list('pin_code')))).replace('"','').replace('[','').replace(']',''),  
           }
          )
  




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
