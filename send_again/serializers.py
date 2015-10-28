from rest_framework import serializers
import random
from random import randint

from register.models import Register, LANGUAGE_CHOICES, STYLE_CHOICES
from django.http import HttpResponse


class Send_againSerializer(serializers.ModelSerializer):
    class Meta:
        model = Register
        fields = ('phone',)
    

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        otp_generated=str(random.randint(100000, 999999))
        #details=validated_data
        #valid=0
        Register.objects.filter(phone=validated_data.get('phone')).update(otp_generated=otp_generated)
        
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
            sms_from='8792213479',  # sms_from='8808891988',
            sms_to=validated_data.get('phone'), # sms_to='9052161119',
            sms_body='Hi '+validated_data.get('phone')+', your number '+otp_generated+' is now turned asOTP')
        print r.status_code
        pprint(r.json())





        def connect_customer_to_agent(sid, token,
                              agent_no, customer_no, callerid,
                              timelimit=None, timeout=None, calltype='trans'):
            return requests.post('https://twilix.exotel.in/v1/Accounts/{sid}/Calls/connect.json'.format(sid=sid),
            auth=(sid, token),
            data= {
                'From': agent_no,
                'To': customer_no,
                'CallerId': callerid,
                'TimeLimit': timelimit,
                'TimeOut': timeout,
                'CallType': calltype
            })


        r = connect_customer_to_agent(
            sid, token,
            agent_no=validated_data.get('phone'),
            customer_no=validated_data.get('phone'),
            callerid="09243422233",
            timelimit="<time-in-seconds>",  # This is optional
            timeout="<time-in-seconds>",  # This is also optional
            calltype="promo"  # Can be "trans" for transactional and "promo" for promotional content
        )

        print r.status_code
        pprint(r.json())

        
 


        return validated_data

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.phone = validated_data.get('phone', instance.phone)
        instance.otp = validated_data.get('otp', instance.otp)
        instance.valid = validated_data.get('valid', instance.valid)
        return instance

        


    from register.models import Register
from send_again.serializers import Send_againSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser



from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    create = serializers.PrimaryKeyRelatedField(many=True, queryset=Register.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'create')

owner = serializers.ReadOnlyField(source='owner.username')

