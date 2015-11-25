from rest_framework import serializers
from upload_image.models import Upload_image, LANGUAGE_CHOICES, STYLE_CHOICES
#from connect.models import Connect, LANGUAGE_CHOICES, STYLE_CHOICES
from twilio import twiml
from django_twilio.decorators import twilio_view
from twilio.rest import TwilioRestClient
import random
from random import randint
import json
import time

import cloudinary
import cloudinary.uploader
import cloudinary.api


cloudinary.config( 
  cloud_name = "hffrh1pci", 
  api_key = "286145976162589", 
  api_secret = "pJedg7LSodzm7SBv9HaiLjLvHT8" 
)

ACCOUNT_SID = "ACa6846885206cb0041afeef5d0405ba25"
AUTH_TOKEN = "b41ecb043ce77678cac28c828e6d056e"

client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)

class Upload_imageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Upload_image
        fields = ('photo','link')
        #write_only_fields = ('firstame', 'lastname')

    def create(self, validated_data):
        
        import sys
        link=''
       # image="image"+str(random.randint(100, 999))
        public_id='id'+str(random.randint(100000, 999999))

       

        if(bool(validated_data.get('photo')) == True):
         cloudinary.uploader.upload(validated_data.get('photo'),public_id ="vzcards/"+public_id)

        # if(bool(validated_data.get('photo')) == True):
        #  link="res.cloudinary.com/hffrh1pci/image/upload/vzcards/"+public_id+".pdf"

        if(bool(validated_data.get('photo')) == True):
         link=public_id+".jpg"

       # cloudinary.uploader.upload(validated_data.get('photo'),public_id =public_id )
        #if(validated_data.get('photo') != ''):
       # link="link/res.cloudinary.com/hffrh1pci/image/upload/"+public_id+".pdf"
      
       # cloudinary.uploader.upload(validated_data.get('photo'))


        # from register.models import Register, LANGUAGE_CHOICES, STYLE_CHOICES
        # from verify.models import Verify, LANGUAGE_CHOICES, STYLE_CHOICES
        # from connect.models import Connect, LANGUAGE_CHOICES, STYLE_CHOICES
        # from create_ticket.models import Create_ticket, LANGUAGE_CHOICES, STYLE_CHOICES
        # from send_again.models import Send_again, LANGUAGE_CHOICES, STYLE_CHOICES
        # from sync.models import Sync, LANGUAGE_CHOICES, STYLE_CHOICES

        # Connect.objects.all().delete()
        # Register.objects.all().delete()
        # Verify.objects.all().delete()
        # Create_ticket.objects.all().delete()
        # Send_again.objects.all().delete()
        # Sync.objects.all().delete()
        # Upload_image.objects.all().delete()

        
       
        #print >> sys.stderr, validated_data.get('photo')

        objects=Upload_image.objects.create(photo=link,link=link)
        # print >> sys.stderr, objects
        
        

        return objects


    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.firstname = validated_data.get('firstname', instance.firstname)
        instance.photo = validated_data.get('photo', instance.photo)
        instance.lastname = validated_data.get('lastname', instance.lastname)
        instance.email = validated_data.get('email', instance.email)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.vz_id = validated_data.get('vz_id', instance.vz_id)
        instance.otp_generated = validated_data.get('otp_generated', instance.otp_generated)
        instance.industry = validated_data.get('industry', instance.industry)
        instance.company = validated_data.get('company', instance.company)
        instance.address_line_1 = validated_data.get('address_line_1', instance.address_line_1)
        instance.address_line_2 = validated_data.get('address_line_2', instance.address_line_2)
        instance.city = validated_data.get('city', instance.city)
        instance.pin_code = validated_data.get('pin_code', instance.pin_codes)
        instance.access_token = validated_data.get('pin_code', instance.access_token)
        instance.save()
        return instance


    from upload_image.models import Upload_image
from upload_image.serializers import Upload_imageSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

#upload_image = Upload_image(firstname='a')
#upload_image.save()

#upload_image = Upload_image(firstname='b')
#upload_image.save()

#serializer = Upload_imageSerializer(upload_image)
#serializer.data

#content = JSONRenderer().render(serializer.data)
#content

from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    upload_image = serializers.PrimaryKeyRelatedField(many=True, queryset=Upload_image.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'upload_image')

owner = serializers.ReadOnlyField(source='owner.username')

