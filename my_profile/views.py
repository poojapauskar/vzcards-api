from user_register.models import User_register
from my_profile.serializers import My_profileSerializer
from rest_framework import generics
# from ticket.permissions import IsOwnerOrReadOnly
# from rest_framework import permissions
from django.shortcuts import get_object_or_404

class My_profileList(generics.ListCreateAPIView):
 queryset = User_register.objects.all()
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

  #vz_id = self.kwargs['vz_id']
     
  #vz_id= Register.objects.filter(token_generated=access_token).values_list('vz_id',flat=True)[0]

  vz_id= User_register.objects.filter(token_generated=access_token).values('vz_id')
  #tickets = Ticket.objects.filter(vz_id__in=contacts)
  print >> sys.stderr, vz_id
  
  
  # profile=[]
  # profile.append(
  #          {
  #           'my_profile':list(Register.objects.filter(vz_id=vz_id).values('pk','token_generated','photo','firstname', 'lastname', 'email', 'phone','vz_id','industry','company','address_line_1','address_line_2','city','pin_code','otp_generated')),  
  #          }
  #         )

  profile=User_register.objects.filter(vz_id=vz_id).values('pk','token_generated','company_photo','photo','firstname', 'lastname','title', 'email', 'phone','vz_id','industry','company','address_line_1','address_line_2','city','pin_code','otp_generated')[0],  
  





  from django.http import JsonResponse
  #return JsonResponse(dict(objects=list(objects)))
  return JsonResponse(profile[0],safe=False)


       

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
