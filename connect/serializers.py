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

       

        if(len(validated_data.get('phone_2'))==12):
         phone=validated_data.get('phone_2')
        else:
         phone="91"+validated_data.get('phone_2')

        if(User_register.objects.filter(phone=validated_data.get('phone_2')).exists()):
         pass
        else:
         if(User_register.objects.filter(vz_id=validated_data.get('connecter_vz_id')).exists):
            name=User_register.objects.get(vz_id=validated_data.get('connecter_vz_id'))
            msg=name.firstname
         else:
            msg="your friend"

         print >> sys.stderr, name
         from pprint import pprint
         import requests
         from django.conf import settings

         #from settings import sid, token
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


        #if __name__ == '__main__':
        # 'From' doesn't matter; For transactional, this will be replaced with your SenderId;
        # For promotional, this will be ignored by the SMS gateway
        # Incase you are wondering who Dr. Rajasekhar is http://en.wikipedia.org/wiki/Dr._Rajasekhar_(actor)
         r = send_message(sid, token,
             sms_from='09243422233',  # sms_from='8808891988',
             sms_to=phone, # sms_to='9052161119',
             sms_body='Hey '+validated_data.get('ticket_id_2')+','+msg+' has shared your contact on VzCards. Checkout this awesome app https://vzcards.com/dl')  # Message body, if any
         print r.status_code
         pprint(r.json())


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

