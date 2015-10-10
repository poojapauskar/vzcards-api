from rest_framework import serializers
from register.models import Register, LANGUAGE_CHOICES, STYLE_CHOICES
from twilio import twiml
from django_twilio.decorators import twilio_view
from twilio.rest import TwilioRestClient
import random
from random import randint
import json



ACCOUNT_SID = "ACa6846885206cb0041afeef5d0405ba25"
AUTH_TOKEN = "b41ecb043ce77678cac28c828e6d056e"

client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)

class RegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Register
        fields = ('pk', 'firstname', 'lastname', 'email', 'phone','vz_id','otp_generated')
        #write_only_fields = ('firstame', 'lastname')

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        
        
        Register.objects.create(**validated_data)
        otp_generated=str(random.randint(100000, 999999));
        Register.objects.filter(phone='918792213479').update(otp_generated=otp_generated)
        #phone =  validated_data
        message = client.messages.create(
         body="Your OTP "+otp_generated,  # Message body, if any
         to="+"+validated_data.get('phone'), #7798899252
         from_="+17028002480",
        )
        #print message.sid

        #otp_generated=str(random.randint(100000, 999999));
        #Register.objects.filter(phone='918792213479').update(otp_generated=otp_generated)

        
        #phone = validated_data.pop('phone')
        # message = client.messages.create(
        #  body=otp_generated,  # Message body, if any
        #  to="+918792213479",
        #  from_="+17028002480",
        # )


        return validated_data


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

