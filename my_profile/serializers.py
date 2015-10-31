from rest_framework import serializers
from register.models import Register, LANGUAGE_CHOICES, STYLE_CHOICES
from my_profile.models import My_profile, LANGUAGE_CHOICES, STYLE_CHOICES

import random
from random import randint

import cloudinary
import cloudinary.uploader
import cloudinary.api


cloudinary.config( 
  cloud_name = "hffrh1pci", 
  api_key = "286145976162589", 
  api_secret = "pJedg7LSodzm7SBv9HaiLjLvHT8" 
)

class My_profileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Register
        fields = ('phone','photo','vz_id','firstname','lastname','email','industry','company','address_line_1','address_line_2','city','pin_code')
        
    def create(self, validated_data): 
 	   

      obj=Register.objects.get(vz_id=validated_data.get('vz_id'))

      link=''
       # image="image"+str(random.randint(100, 999))
      public_id='id'+str(random.randint(100, 999))

     

      if(bool(validated_data.get('photo')) == True):
       cloudinary.uploader.upload(validated_data.get('photo'),public_id =public_id )

      if(bool(validated_data.get('photo')) == True):
       link="link/res.cloudinary.com/hffrh1pci/image/upload/"+public_id+".pdf"

      

      objects=Register.objects.filter(vz_id=validated_data.get('vz_id')).update(phone=obj.phone,photo=link,firstname=validated_data.get('firstname'),lastname=validated_data.get('lastname'),email=validated_data.get('email'),industry=validated_data.get('industry'),company=validated_data.get('company'),address_line_1=validated_data.get('address_line_1'),address_line_2=validated_data.get('address_line_2'),city=validated_data.get('city'),pin_code=validated_data.get('pin_code'))
      
      objects1=Register.objects.filter(vz_id=validated_data.get('vz_id')).values('phone','photo','vz_id','firstname','lastname','email','industry','company','address_line_1','address_line_2','city','pin_code')
      from django.http import JsonResponse
      #return JsonResponse(dict(objects=list(objects)))
      return JsonResponse((list(objects1)),safe=False)

      #return objects

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.firstname = validated_data.get('firstname', instance.firstname)
        instance.lastname = validated_data.get('lastname', instance.lastname)
        instance.email = validated_data.get('email', instance.email)
        instance.vz_id = validated_data.get('vz_id', instance.vz_id)
        instance.industry = validated_data.get('industry', instance.industry)
        instance.company = validated_data.get('company', instance.company)
        instance.address_line_1 = validated_data.get('address_line_1', instance.address_line_1)
        instance.address_line_2 = validated_data.get('address_line_2', instance.address_line_2)
        instance.city = validated_data.get('city', instance.city)
        instance.pin_code = validated_data.get('pin_code', instance.pin_codes)
        instance.photo = validated_data.get('photo', instance.photo)
        instance.save()
        return instance

from ticket_create.models import Ticket_create
from my_profile.serializers import My_profileSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser




from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    create = serializers.PrimaryKeyRelatedField(many=True, queryset=Register.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'create')

owner = serializers.ReadOnlyField(source='owner.username')

