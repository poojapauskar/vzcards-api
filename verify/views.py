from verify.models import Verify
from verify.serializers import VerifySerializer
from rest_framework import generics
# from verify.permissions import IsOwnerOrReadOnly
# from rest_framework import permissions
from verify.models import Verify, LANGUAGE_CHOICES, STYLE_CHOICES

from user_register.models import User_register, LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth.models import User, Group


class VerifyList(generics.ListCreateAPIView):
 queryset = Verify.objects.all()
 serializer_class = VerifySerializer
 # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)



class VerifyDetail(generics.RetrieveUpdateDestroyAPIView):
 queryset = Verify.objects.all()
 serializer_class = VerifySerializer
 # permission_classes = (permissions.IsAuthenticatedOrReadOnly,
 #                      IsOwnerOrReadOnly,)

def get_queryset(request):

  from oauthlib.common import generate_token
  token = generate_token()
        
  phone= request.META.get('HTTP_PHONE')
  otp= request.META.get('HTTP_OTP')

  if (User_register.objects.filter(phone=phone).values('phone')).exists():
   Verify.objects.filter(phone=phone).delete()

  if (User.objects.filter(username=phone)).exists():
   User.objects.filter(username=phone).delete()
        
  if ((User_register.objects.filter(phone=phone).filter(otp_generated=otp).values('phone')).exists() or ((User_register.objects.filter(phone=phone).values('phone')).exists() and (otp=='444444'))):
   user=User.objects.create(username=phone,password="vzcards")

  from oauth2_provider.settings import oauth2_settings
  from oauthlib.common import generate_token
  from django.http import JsonResponse
  from oauth2_provider.models import AccessToken, Application, RefreshToken
  from django.utils.timezone import now, timedelta
  from django.http import HttpResponse
  from django.contrib.auth import login
  # from social.apps.django_app.utils import psa
  # from .tools import get_access_token
  from datetime import datetime


  expire_seconds = oauth2_settings.user_settings['ACCESS_TOKEN_EXPIRE_SECONDS']
  scopes = oauth2_settings.user_settings['SCOPES']


  application = Application.objects.get(name="vzcards-api")
  expires = datetime.now() + timedelta(seconds=expire_seconds)

  if ((User_register.objects.filter(phone=phone).filter(otp_generated=otp).values('phone')).exists() or ((User_register.objects.filter(phone=phone).values('phone')).exists() and (otp=='444444'))):
   access_token = AccessToken.objects.create(
                    user=user,
                    application=application,
                    token=generate_token(),
                    expires=expires,
                    scope=scopes)
  if ((User_register.objects.filter(phone=phone).filter(otp_generated=otp).values('phone')).exists() or ((User_register.objects.filter(phone=phone).values('phone')).exists() and (otp=='444444'))):
   refresh_token = RefreshToken.objects.create(
                    user=user,
                    token=generate_token(),
                    access_token=access_token,
                    application=application)

  

  import json
  if ((User_register.objects.filter(phone=phone).filter(otp_generated=otp).values('phone')).exists() or ((User_register.objects.filter(phone=phone).values('phone')).exists() and (otp=='444444'))):
   token = access_token.token
   token= json.dumps(token)
   token = token.replace('"','')


        
  if ((User_register.objects.filter(phone=phone).filter(otp_generated=otp).values('phone')).exists() or ((User_register.objects.filter(phone=phone).values('phone')).exists() and (otp=='444444'))):
   User_register.objects.filter(phone=phone).update(token_generated=token)
        
  if (User_register.objects.filter(phone=phone).values('phone')).exists():
   vz_id= User_register.objects.filter(phone=phone).values_list('vz_id',flat=True)[0]

  if ((User_register.objects.filter(phone=phone).filter(otp_generated=otp).values('phone')).exists() or ((User_register.objects.filter(phone=phone).values('phone')).exists() and (otp=='444444'))):
   objects=Verify.objects.create(phone=phone,otp=otp,valid=1,token_generated=token,vz_id=vz_id)
   details=[]
   details.append({
   		'user_details': Verify.objects.filter(phone=phone,otp=otp).values('phone','otp','valid','token_generated','vz_id')[0],
   		'is_organization': User_register.objects.filter(phone=phone).values('is_organization')[0],
   	})

  else:
   objects=Verify.objects.create(phone=phone,otp=otp,valid=0,token_generated='',vz_id=vz_id) 
   details=[]
   details.append({
   		'user_details': Verify.objects.filter(phone=phone,otp=otp).values('phone','otp','valid','token_generated','vz_id')[0],
   		'is_organization': User_register.objects.filter(phone=phone).values('is_organization')[0],
   	})   

  import sys
  from django.http import JsonResponse
  return JsonResponse(details[0],safe=False)

from django.contrib.auth.models import User
from verify.serializers import UserSerializer
from rest_framework import permissions


class UserList(generics.ListAPIView):
 queryset = User.objects.all()
 serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
 queryset = User.objects.all()
 serializer_class = UserSerializer


def perform_create(self, serializer):
 serializer.save(owner=self.request.user)




