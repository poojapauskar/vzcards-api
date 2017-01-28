from rest_framework import serializers
from connect.models import Connect, LANGUAGE_CHOICES, STYLE_CHOICES
from user_register.models import User_register, LANGUAGE_CHOICES, STYLE_CHOICES
from ticket_create.models import Ticket_create, LANGUAGE_CHOICES, STYLE_CHOICES



class ConnectSerializer(serializers.ModelSerializer):
    class Meta:

        model = User_register
        fields = ('firstname',)
    
        model = Connect
        fields = ('connecter_vz_id','phone_1', 'ticket_id_1', 'phone_2', 'ticket_id_2','my_ticket','reffered_ticket','reffered_phone')
    

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        
        import json
        Connect.objects.create(connecter_vz_id=validated_data.get('connecter_vz_id'),my_ticket=validated_data.get('ticket_id_1'),reffered_ticket=validated_data.get('ticket_id_2'),reffered_phone=validated_data.get('phone_2'))
        Connect.objects.create(connecter_vz_id=validated_data.get('connecter_vz_id'),my_ticket=validated_data.get('ticket_id_2'),reffered_ticket=validated_data.get('ticket_id_1'),reffered_phone=validated_data.get('phone_1'))
        
        from twilio import twiml
        from django_twilio.decorators import twilio_view
        from twilio.rest import TwilioRestClient

        ACCOUNT_SID = "ACa6846885206cb0041afeef5d0405ba25"
        AUTH_TOKEN = "b41ecb043ce77678cac28c828e6d056e"

        import sys
        print >> sys.stderr, validated_data.get('connecter_vz_id')

       

        # if(len(validated_data.get('phone_2'))==12):
        phone=validated_data.get('phone_2')
        # else:
        #  phone="91"+validated_data.get('phone_2')

        if(User_register.objects.filter(phone=validated_data.get('phone_2')).exists()):
         name=User_register.objects.get(vz_id=validated_data.get('connecter_vz_id'))
         if(name.firstname==''):
          msg="your friend"
         else:
          msg=name.firstname

         print >> sys.stderr, msg
         

         import sys
         print sys.stderr, phone


         user_1_details=User_register.objects.get(phone=validated_data.get('phone_1'))
         connecter_name_details=User_register.objects.get(vz_id=validated_data.get('connecter_vz_id'))

         if(user_1_details.firstname == '' and user_1_details.lastname == ''):
          user_1_name='contact'
         elif(user_1_details.firstname == ''):
          user_1_name=user_1_details.lastname
         elif(user_1_details.lastname == ''):
          user_1_name=user_1_details.firstname
         else:
          user_1_name=user_1_details.firstname+' '+user_1_details.lastname

         if(connecter_name_details.firstname == '' and connecter_name_details.lastname == ''):
          connecter_name=connecter_name_details.phone
         elif(connecter_name_details.firstname == ''):
          connecter_name=connecter_name_details.lastname
         elif(connecter_name_details.lastname == ''):
          connecter_name=connecter_name_details.firstname
         else:
          connecter_name=connecter_name_details.firstname+' '+connecter_name_details.lastname

         if(str(phone)[:2] == '91'):
          print sys.stderr, "Indian Numbers" 
          ## Exotel messages------------------------------------------------
          from pprint import pprint
          import requests
          from django.conf import settings

          #from settings import sid, token
          # sid = 'bitjini2'
          # token = 'e064d27250bdd098a3aca1822adf24e1039d219a'

          # def send_message(sid, token, sms_from, sms_to, sms_body):
          #  return requests.post('https://twilix.exotel.in/v1/Accounts/{sid}/Sms/send.json'.format(sid=sid),
          #  auth=(sid, token),
          #  data={
          #    'From': sms_from,
          #    'To': sms_to,
          #    'Body': sms_body
          #  })

          # r = send_message(sid, token,
          #  sms_from='08030752644',  # sms_from='8808891988',
          #  sms_to=phone, # sms_to='9052161119',
          #  sms_body='Dear '+validated_data.get('ticket_id_2')+',%0Ayour friend '+validated_data.get('connecter_vz_id')+' has referred you to '+user_1_name+' for a "Ticket". '+user_1_details.firstname+' '+user_1_details.lastname+' phone no. - '+validated_data.get('phone_1'))
          # print r.status_code
          # pprint(r.json())

          connect_msg="http://enterprise.smsgupshup.com/GatewayAPI/rest?msg=Dear "+validated_data.get('ticket_id_2')+",%0Ayour friend "+connecter_name+" has referred you to "+user_1_name+" for a 'Ticket'. "+user_1_details.firstname+" "+user_1_details.lastname+" phone no. - "+validated_data.get('phone_1')+".&v=1.1&userid=2000159262&password=ZtIA4TyB1&send_to="+phone+"&msg_type=text&method=sendMessage"
          
          import requests
          r = requests.get(connect_msg)
          r.status_code

        ##--------------------------------------------


         else:
          print sys.stderr, "International Numbers" 
          # Nexmo messages
          import urllib
          import urllib2

          params = {
           'api_key': '24def3ee',
           'api_secret': '865357d5',
           'to': phone,
           'from': 'NEXMO',
           'text': 'Dear '+validated_data.get('ticket_id_2')+',%0Ayour friend '+connecter_name+' has referred you to '+user_1_name+' for a "Ticket". '+user_1_details.firstname+' '+user_1_details.lastname+' phone no. - '+validated_data.get('phone_1')
          }

          url = 'https://rest.nexmo.com/sms/json?' + urllib.urlencode(params)

          request = urllib2.Request(url)
          request.add_header('Accept', 'application/json')
          response = urllib2.urlopen(request)
        else:
         name=User_register.objects.get(vz_id=validated_data.get('connecter_vz_id'))
         if(name.firstname==''):
          msg="your friend"
         else:
          msg=name.firstname

         print >> sys.stderr, msg
         

         import sys
         print sys.stderr, phone

         if(str(phone)[:2] == '91'):
          print sys.stderr, "Indian Numbers" 
          ## Exotel messages------------------------------------------------
          from pprint import pprint
          import requests
          from django.conf import settings

          #from settings import sid, token
          # sid = 'bitjini2'
          # token = 'e064d27250bdd098a3aca1822adf24e1039d219a'

          # def send_message(sid, token, sms_from, sms_to, sms_body):
          #  return requests.post('https://twilix.exotel.in/v1/Accounts/{sid}/Sms/send.json'.format(sid=sid),
          #  auth=(sid, token),
          #  data={
          #    'From': sms_from,
          #    'To': sms_to,
          #    'Body': sms_body
          #  })


          # r = send_message(sid, token,
          #  sms_from='08030752644',  # sms_from='8808891988',
          #  sms_to=phone, # sms_to='9052161119',
          #  sms_body='Hey '+validated_data.get('ticket_id_2')+','+msg+' has shared your contact on VzCards. Checkout this awesome app https://vzcards.com/dl')  # Message body, if any
          # print r.status_code
          # pprint(r.json())
        ##--------------------------------------------
          connect_msg="http://enterprise.smsgupshup.com/GatewayAPI/rest?msg=Hey "+validated_data.get('ticket_id_2')+","+msg+" has shared your contact on VzCards. Checkout this awesome app https://vzcards.com/dl&v=1.1&userid=2000159262&password=ZtIA4TyB1&send_to="+phone+"&msg_type=text&method=sendMessage"
          
          import requests
          r = requests.get(connect_msg)
          r.status_code

         else:
          print sys.stderr, "International Numbers" 
          # Nexmo messages
          import urllib
          import urllib2

          params = {
           'api_key': '24def3ee',
           'api_secret': '865357d5',
           'to': phone,
           'from': 'NEXMO',
           'text': 'Hey '+validated_data.get('ticket_id_2')+','+msg+' has shared your contact on VzCards. Checkout this awesome app https://vzcards.com/dl'  # Message body, if any
          }

          url = 'https://rest.nexmo.com/sms/json?' + urllib.urlencode(params)

          request = urllib2.Request(url)
          request.add_header('Accept', 'application/json')
          response = urllib2.urlopen(request)


         # message = client.messages.create(
         #  body="Hey "+validated_data.get('ticket_id_2')+", "+name+"has shared your contact on VzCards, checkout this awesomes app https://vzcards.com/dl",  # Message body, if any
         #  to=phone, #7798899252
         #  from_="+17028002480",
         # )

        
        

        


        return validated_data


    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.connecter_vz_id = validated_data.get('connecter_vz_id', instance.connecter_vz_id)
        instance.phone_1 = validated_data.get('phone_1', instance.phone_1)
        instance.ticket_id_1 = validated_data.get('ticket_id_1', instance.ticket_id_1)
        instance.phone_2 = validated_data.get('phone_2', instance.phone_2)
        instance.ticket_id_2 = validated_data.get('ticket_id_2', instance.ticket_id_2)
        # instance.connecter_details = validated_data.get('connecter_details', instance.connecter_details)
        # instance.ticket_1_details = validated_data.get('ticket_1_details', instance.ticket_1_details)
        # instance.ticket_2_details = validated_data.get('ticket_2_details', instance.ticket_2_details)
        # instance.phone_1_details = validated_data.get('phone_1_details', instance.phone_1_details)
        # instance.phone_2_details = validated_data.get('phone_2_details', instance.phone_2_details)
        instance.save()


        return instance

#person1 has shared ur contact on VzCards. 

    from connect.models import Connect
from connect.serializers import ConnectSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser



from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    connect = serializers.PrimaryKeyRelatedField(many=True, queryset=Connect.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'connect')

owner = serializers.ReadOnlyField(source='owner.username')

