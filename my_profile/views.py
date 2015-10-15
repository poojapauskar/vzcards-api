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


class My_profileDetail(generics.ListCreateAPIView):
 serializer_class = My_profileSerializer

 def get_queryset(self):
  vz_id = self.kwargs['vz_id']
        
  # Register.objects.filter(vz_id=vz_id).update(firstname=validated_data.get('firstname'),lastname=validated_data.get('lastname'),email=validated_data.get('email'),industry=validated_data.get('industry'),address_line_1=validated_data.get('address_line_1'),address_line_2=validated_data.get('address_line_2'),city=validated_data.get('city'),pin_code=validated_data.get('pin_code'))
 


  profile=Register.objects.filter(vz_id=vz_id)

   
 #def create(self, validated_data):
        
 # 	#vz_id = self.kwargs['vz_id']

 # 	     # if (validated_data.get('firstname') != ''):
 #       #   	objects=Register.objects.filter(vz_id=vz_id).update(firstname=validated_data.get('firstname'))
 #       #  if (validated_data.get('lastname') != ''):
 #       #   	objects=Register.objects.filter(vz_id=vz_id).update(lastname=validated_data.get('lastname'))
 #       #  if (validated_data.get('email') != ''):
 #       #   	objects=Register.objects.filter(vz_id=vz_id).update(email=validated_data.get('email'))
 #       #  if (validated_data.get('industry') != ''):
 #       #   	objects=Register.objects.filter(vz_id=vz_id).update(industry=validated_data.get('industry'))
 #       #  if (validated_data.get('address_line_1') != ''):
 #       #   	objects=Register.objects.filter(vz_id=vz_id).update(address_line_1=validated_data.get('address_line_1'))
 #       #  if (validated_data.get('address_line_2') != ''):
 #       #   	objects=Register.objects.filter(vz_id=vz_id).update(address_line_2=validated_data.get('address_line_2'))
 #       #  if (validated_data.get('city') != ''):
 #       #   	objects=Register.objects.filter(vz_id=vz_id).update(city=validated_data.get('city'))
 #       #  if (validated_data.get('pin_code') != ''):
 #       #   	objects=Register.objects.filter(vz_id=vz_id).update(pin_code=validated_data.get('pin_code'))


 #  # Register.objects.filter(vz_id=vz_id).update(firstname=validated_data.get('firstname'),lastname=validated_data.get('lastname'),email=validated_data.get('email'),industry=validated_data.get('industry'),address_line_1=validated_data.get('address_line_1'),address_line_2=validated_data.get('address_line_2'),city=validated_data.get('city'),pin_code=validated_data.get('pin_code'))
 #  return validated_data
  return profile
       

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
