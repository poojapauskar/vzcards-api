from rest_framework import serializers
from user_register.models import User_register, LANGUAGE_CHOICES, STYLE_CHOICES
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

class User_registerSerializer(serializers.ModelSerializer):

    class Meta:
        model = User_register
        fields = ('pk','token_generated','company_photo','photo','firstname', 'lastname', 'email', 'phone','vz_id','industry','company','address_line_1','address_line_2','city','pin_code','otp_generated')
        #write_only_fields = ('firstame', 'lastname')

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        
        # from ticket.models import Ticket, LANGUAGE_CHOICES, STYLE_CHOICES
        # from verify.models import Verify, LANGUAGE_CHOICES, STYLE_CHOICES
        # from sync.models import Sync, LANGUAGE_CHOICES, STYLE_CHOICES
        #User_register.objects.all().delete()
        # Verify.objects.all().delete()
        # Sync.objects.all().delete()
        # Ticket.objects.all().delete()

        
        #User_register.objects.create(**validated_data)
        otp_generated=str(random.randint(100000, 999999))
        vz_id='VZ'+str(int(time.time()))
       
        # User_register.objects.filter(phone=validated_data.get('phone')).update(otp_generated=otp_generated)
        # User_register.objects.filter(phone=validated_data.get('phone')).update(vz_id=vz_id)
        #phone =  validated_data
        

        # message = client.messages.create(
        #  body="Your OTP "+otp_generated,  # Message body, if any
        #  to="+"+validated_data.get('phone'), #7798899252
        #  from_="+17028002480",
        # )
        
        ##------------------------------------------------
        from pprint import pprint
        import requests
        from django.conf import settings
        
        sid = 'bitjini2'
        token = 'e064d27250bdd098a3aca1822adf24e1039d219a'

        def send_message(sid, token, sms_from, sms_to, sms_body):
            return requests.post('https://twilix.exotel.in/v1/Accounts/{sid}/Sms/send.json'.format(sid=sid),
            auth=(sid, token),
            data={
                'From': sms_from,
                'To': sms_to,
                'Body': sms_body
            })


        #if __name__ == '__main__':
        # 'From' doesn't matter; For transactional, this will be replaced with your SenderId;
        # For promotional, this will be ignored by the SMS gateway
        # Incase you are wondering who Dr. Rajasekhar is http://en.wikipedia.org/wiki/Dr._Rajasekhar_(actor)
        r = send_message(sid, token,
            sms_from='08030752644',  # sms_from='8808891988',
            sms_to=validated_data.get('phone'), # sms_to='9052161119',
            sms_body='Hi '+validated_data.get('phone')+', Your one time password for VzCards login is 999999. Please use the password to login to the app.')
        print r.status_code
        pprint(r.json())
        ##--------------------------------------------
        from django.http import HttpResponse
        from django.http import JsonResponse
        
       
        if User_register.objects.filter(phone=validated_data.get('phone')).exists():
          User_register.objects.filter(phone=validated_data.get('phone')).update(otp_generated='999999')
        if User_register.objects.filter(phone=validated_data.get('phone')).exists():
          return validated_data
        import sys
       
       # cloudinary.uploader.upload(validated_data.get('photo'),public_id =public_id )
        #if(validated_data.get('photo') != ''):
       # link="link/res.cloudinary.com/hffrh1pci/image/upload/"+public_id+".pdf"
      
       # cloudinary.uploader.upload(validated_data.get('photo'))

       # link="http://res.cloudinary.com/hjwxtjtff/image/upload/"+public_id+".pdf"
        #print >> sys.stderr, validated_data.get('photo')
        objects=User_register.objects.create(token_generated='',company_photo=validated_data.get('company_photo'),photo=validated_data.get('photo'),firstname=validated_data.get('firstname'),lastname=validated_data.get('lastname'),email=validated_data.get('email'),phone=validated_data.get('phone'),vz_id=vz_id,otp_generated='999999',industry=validated_data.get('industry'),company=validated_data.get('company'),address_line_1=validated_data.get('address_line_1'),address_line_2=validated_data.get('address_line_2'),city=validated_data.get('city'),pin_code=validated_data.get('pin_code'))
        # print >> sys.stderr, objects
        


        return objects


    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.firstname = validated_data.get('firstname', instance.firstname)
        instance.photo = validated_data.get('photo', instance.photo)
        instance.company_photo = validated_data.get('company_photo', instance.company_photo)
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


    from user_register.models import User_register
from user_register.serializers import User_registerSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

#user_register = User_register(firstname='a')
#user_register.save()

#user_register = User_register(firstname='b')
#user_register.save()

#serializer = User_registerSerializer(user_register)
#serializer.data

#content = JSONRenderer().render(serializer.data)
#content

from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    user_register = serializers.PrimaryKeyRelatedField(many=True, queryset=User_register.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'user_register')

owner = serializers.ReadOnlyField(source='owner.username')
