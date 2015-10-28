from rest_framework import serializers
from register.models import Register, LANGUAGE_CHOICES, STYLE_CHOICES
from twilio import twiml
from django_twilio.decorators import twilio_view
from twilio.rest import TwilioRestClient
import random
from random import randint
import json
import time



ACCOUNT_SID = "ACa6846885206cb0041afeef5d0405ba25"
AUTH_TOKEN = "b41ecb043ce77678cac28c828e6d056e"

client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)

class RegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Register
        fields = ('pk','token_generated', 'firstname', 'lastname', 'email', 'phone','vz_id','industry','company','address_line_1','address_line_2','city','pin_code','otp_generated')
        #write_only_fields = ('firstame', 'lastname')

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        
        
        #Register.objects.create(**validated_data)
        otp_generated=str(random.randint(100000, 999999))
        vz_id='VZ'+str(int(time.time()))
       
        # Register.objects.filter(phone=validated_data.get('phone')).update(otp_generated=otp_generated)
        # Register.objects.filter(phone=validated_data.get('phone')).update(vz_id=vz_id)
        #phone =  validated_data
        

        message = client.messages.create(
         body="Your OTP "+otp_generated,  # Message body, if any
         to="+"+validated_data.get('phone'), #7798899252
         from_="+17028002480",
        )
        
        
        #Register.objects.all().delete()
        # if Register.objects.filter(phone=validated_data.get('phone')).exists():
        #  return validated_data
        

        objects=Register.objects.create(token_generated='',firstname=validated_data.get('firstname'),lastname=validated_data.get('lastname'),email=validated_data.get('email'),phone=validated_data.get('phone'),vz_id=vz_id,otp_generated=otp_generated,industry=validated_data.get('industry'),company=validated_data.get('company'),address_line_1=validated_data.get('address_line_1'),address_line_2=validated_data.get('address_line_2'),city=validated_data.get('city'),pin_code=validated_data.get('pin_code'))
        
        # from ticket.models import Ticket, LANGUAGE_CHOICES, STYLE_CHOICES
        # # from verify.models import Verify, LANGUAGE_CHOICES, STYLE_CHOICES
        # # from sync.models import Sync, LANGUAGE_CHOICES, STYLE_CHOICES
        # Register.objects.all().delete()
        # # Verify.objects.all().delete()
        # # Sync.objects.all().delete()
        # Ticket.objects.all().delete()



        return objects
#------------------------------------------------------------------------
#         from django.http import HttpResponse
#         from django.contrib.auth import login
 
# # When we send a third party access token to that view
# # as a GET request with access_token parameter, 
# # python social auth communicate with
# # the third party and request the user info to register or
# # sign in the user. Magic. Yeah.
#         def register_by_access_token(request, backend):
 
#          token = request.GET.get('access_token')
#     # here comes the magic
#          user = request.backend.do_auth(token)
#          if user:
#           login(request, user)
#         # that function will return our own
#         # OAuth2 token as JSON
#         # Normally, we wouldn't necessarily return a new token, but you get the idea
#           return get_access_token(user)
#          else:
#         # If there was an error... you decide what you do here
#           return HttpResponse("error")
        
#         def get_access_token(user):
#          from oauth2_provider.settings import oauth2_settings
#          from oauthlib.common import generate_token
#          from django.http import JsonResponse
#          from oauth2_provider.models import AccessToken, Application, RefreshToken
#          from django.utils.timezone import now, timedelta
#          from django.http import HttpResponse
#          from django.contrib.auth import login
#          from social.apps.django_app.utils import psa
#          from .tools import get_access_token
       
#          app = Application.objects.get(name="vzcards")

 
#     # we generate an access token
#          token = generate_token()
#     # we generate a refresh token
#          refresh_token = generate_token()
 
#          expires = now() + timedelta(seconds=oauth2_settings.
#                                 ACCESS_TOKEN_EXPIRE_SECONDS)
#          scope = "read write"
        
#          access_token = AccessToken.objects.\
#          create(user=user,
#                application=app,
#                expires=expires,
#                token=token,
#                scope=scope)
 
#         # we create the refresh token
#          RefreshToken.objects.\
#          create(user=user,
#                application=app,
#                token=refresh_token,
#                access_token=access_token)
 

#          objects1=Register.objects.create(firstname=validated_data.get('firstname'),lastname=validated_data.get('lastname'),email=validated_data.get('email'),phone=validated_data.get('phone'),vz_id=vz_id,otp_generated=otp_generated,industry=access_token,company=validated_data.get('company'),address_line_1=validated_data.get('address_line_1'),address_line_2=validated_data.get('address_line_2'),city=validated_data.get('city'),pin_code=validated_data.get('pin_code'))
#          return objects1

#-----------------------------------------------------------
        


    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.firstname = validated_data.get('firstname', instance.firstname)
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

