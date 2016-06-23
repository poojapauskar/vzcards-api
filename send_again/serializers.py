from rest_framework import serializers
import random
from random import randint

from user_register.models import User_register, LANGUAGE_CHOICES, STYLE_CHOICES
from django.http import HttpResponse


class Send_againSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_register
        fields = ('phone',)
    

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        otp_generated=str(random.randint(100000, 999999))
        #details=validated_data
        #valid=0
        User_register.objects.filter(phone=validated_data.get('phone')).update(otp_generated=otp_generated)
        
        # NEXMO_USERNAME = 'pooja'
        # NEXMO_PASSWORD = 'Pooja22222'
        # NEXMO_FROM = 'vzcards'

        # from nexmo import send_message
        # send_message('+918792213479', 'My sms message body')

        # from nexmo.libpynexmo.nexmomessage import NexmoMessage
        # params = {
        #     'api_key': '24def3ee',
        #     'api_secret': '865357d5',
        #     'type': 'unicode',
        #     'from': settings.NEXMO_FROM,
        #     'to': "+"+validated_data.get('phone'),
        #     'text': "'our OTP "+otp_generated,
        # }
        # sms = NexmoMessage(params)
        # response = sms.send_request()



        import sys
        print sys.stderr, validated_data.get('phone')

        if(str(validated_data.get('phone'))[:2] == '91'):
          print sys.stderr, "Indian Numbers" 
          ## Exotel messages------------------------------------------------
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


    
          r = send_message(sid, token,
              sms_from='08030752644',  
              sms_to=validated_data.get('phone'), 
              sms_body='Hi '+validated_data.get('phone')+', Your one time password for VzCards login is '+otp_generated+'. Please use the password to login to the app.')
          print r.status_code
          pprint(r.json())
          ##--------------------------------------------
        

        else:
          print sys.stderr, "International Numbers" 
          # Nexmo messages
          import urllib
          import urllib2

          params = {
              'api_key': '24def3ee',
              'api_secret': '865357d5',
              'to': validated_data.get('phone'),
              'from': 'NEXMO',
              'text': 'Hi '+validated_data.get('phone')+', Your one time password for VzCards login is '+otp_generated+'. Please use the password to login to the app.'
          }

          url = 'https://rest.nexmo.com/sms/json?' + urllib.urlencode(params)

          request = urllib2.Request(url)
          request.add_header('Accept', 'application/json')
          response = urllib2.urlopen(request)

        #-----------------------------





        # def connect_customer_to_agent(sid, token,
        #                       agent_no, customer_no, callerid,
        #                       timelimit=None, timeout=None, calltype='trans'):
        #     return requests.post('https://twilix.exotel.in/v1/Accounts/{sid}/Calls/connect.json'.format(sid=sid),
        #     auth=(sid, token),
        #     data= {
        #         'From': agent_no,
        #         'To': customer_no,
        #         'CallerId': callerid,
        #         'TimeLimit': timelimit,
        #         'TimeOut': timeout,
        #         'CallType': calltype
        #     })


        # r = connect_customer_to_agent(
        #     sid, token,
        #     agent_no=validated_data.get('phone'),
        #     customer_no=validated_data.get('phone'),
        #     callerid="08039534803",
        #     timelimit="<time-in-seconds>",  
        #     timeout="<time-in-seconds>", 
        #     calltype="promo" 
        # )

        # print r.status_code
        # pprint(r.json())

        
 


        return validated_data

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.phone = validated_data.get('phone', instance.phone)
        instance.otp = validated_data.get('otp', instance.otp)
        instance.valid = validated_data.get('valid', instance.valid)
        return instance

        


    from user_register.models import User_register
from send_again.serializers import Send_againSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser



from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    create = serializers.PrimaryKeyRelatedField(many=True, queryset=User_register.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'create')

owner = serializers.ReadOnlyField(source='owner.username')

