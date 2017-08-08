from rest_framework import serializers
from register.models import Register, LANGUAGE_CHOICES, STYLE_CHOICES
from twilio import twiml
# from django_twilio.decorators import twilio_view
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

class RegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Register
        fields = ('otp_created_time','pk','token_generated','photo','firstname', 'lastname', 'email', 'phone','vz_id','industry','company','address_line_1','address_line_2','city','pin_code','otp_generated')
        #write_only_fields = ('firstame', 'lastname')

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        
        # from ticket.models import Ticket, LANGUAGE_CHOICES, STYLE_CHOICES
        # from verify.models import Verify, LANGUAGE_CHOICES, STYLE_CHOICES
        # from sync.models import Sync, LANGUAGE_CHOICES, STYLE_CHOICES
        #Register.objects.all().delete()
        # Verify.objects.all().delete()
        # Sync.objects.all().delete()
        # Ticket.objects.all().delete()

        import datetime
        current_time= datetime.datetime.now()

        if(Register.objects.filter(phone=validated_data.get('phone')).exists()):
         obj1=Register.objects.filter(phone=validated_data.get('phone')).values('otp_created_time','otp_generated')
         otp_time1= obj1[0]['otp_created_time']
         if(otp_time1 == ""):
          otp_generated=str(random.randint(100000, 999999))
         else:
          otp_time1= datetime.datetime.strptime(otp_time1, "%Y-%m-%d %H:%M:%S.%f")
          diff=(current_time-otp_time1).seconds
          print "diff"
          print diff
          if(diff > 300):
           otp_generated=str(random.randint(100000, 999999))
          else:
           otp_generated=obj1[0]['otp']
        else:
         otp_generated=str(random.randint(100000, 999999)) 
        

        print "---------datetime.datetime.now()---------------"
        otp_created_time= datetime.datetime.now()
        print otp_created_time
        
        #Register.objects.create(**validated_data)
        # otp_generated=str(random.randint(100000, 999999))
        vz_id='VZ'+str(int(time.time()))
       
        # Register.objects.filter(phone=validated_data.get('phone')).update(otp_generated=otp_generated)
        # Register.objects.filter(phone=validated_data.get('phone')).update(vz_id=vz_id)
        #phone =  validated_data

        from pprint import pprint
        import requests
        from django.conf import settings
        
        sid = 'bitjini'
        token = '85dbbbc18dfaf078290eeee3c185ac6dfd8a208f'

        def send_message(sid, token, sms_from, sms_to, sms_body):
            return requests.post('https://twilix.exotel.in/v1/Accounts/{sid}/Sms/send.json'.format(sid=sid),
            auth=(sid, token),
            data={
                'From': sms_from,
                'To': sms_to,
                'Body': sms_body
            })


        
        r = send_message(sid, token,
            sms_from='09243422233',  # sms_from='8808891988',
            sms_to=validated_data.get('phone'), # sms_to='9052161119',
            sms_body='Hi '+validated_data.get('phone')+', your number '+otp_generated+' is now turned asOTP.')
        print r.status_code
        pprint(r.json())


        # r=requests.post('http://enterprise.smsgupshup.com/GatewayAPI/rest?method=SendMessage&send_to=918792213479&msg=Hello&msg_type=TEXT&userid=2000159262&auth_scheme=plain&password=ZtIA4TyB1&v=1.1&format=text')
        # import sys
        # print sys.stderr,r
        
        from django.http import HttpResponse
        from django.http import JsonResponse
        
       
        if Register.objects.filter(phone=validated_data.get('phone')).exists():
          Register.objects.filter(phone=validated_data.get('phone')).update(otp_generated=otp_generated,otp_created_time=otp_created_time)
        if Register.objects.filter(phone=validated_data.get('phone')).exists():
          return validated_data
        import sys
       
       # cloudinary.uploader.upload(validated_data.get('photo'),public_id =public_id )
        #if(validated_data.get('photo') != ''):
       # link="link/res.cloudinary.com/hffrh1pci/image/upload/"+public_id+".pdf"
      
       # cloudinary.uploader.upload(validated_data.get('photo'))

       # link="http://res.cloudinary.com/hjwxtjtff/image/upload/"+public_id+".pdf"
        #print >> sys.stderr, validated_data.get('photo')
        objects=Register.objects.create(otp_created_time=otp_created_time,token_generated='',photo=validated_data.get('photo'),firstname=validated_data.get('firstname'),lastname=validated_data.get('lastname'),email=validated_data.get('email'),phone=validated_data.get('phone'),vz_id=vz_id,otp_generated=otp_generated,industry=validated_data.get('industry'),company=validated_data.get('company'),address_line_1=validated_data.get('address_line_1'),address_line_2=validated_data.get('address_line_2'),city=validated_data.get('city'),pin_code=validated_data.get('pin_code'))
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
        instance.otp_created_time = validated_data.get('otp_created_time', instance.otp_created_time)
        instance.save()
        return instance


    from register.models import Register
from register.serializers import RegisterSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

#register = Register(firstname='a')
#register.save()

#register = Register(firstname='b')
#register.save()

#serializer = RegisterSerializer(register)
#serializer.data

#content = JSONRenderer().render(serializer.data)
#content

from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    register = serializers.PrimaryKeyRelatedField(many=True, queryset=Register.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'register')

owner = serializers.ReadOnlyField(source='owner.username')
