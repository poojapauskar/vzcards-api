from rest_framework import serializers
from connect.models import Connect, LANGUAGE_CHOICES, STYLE_CHOICES
from register.models import Register, LANGUAGE_CHOICES, STYLE_CHOICES
from ticket_create.models import Ticket_create, LANGUAGE_CHOICES, STYLE_CHOICES



class ConnectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Connect
        fields = ('connecter_vz_id','phone_1', 'ticket_id_1', 'phone_2', 'ticket_id_2')
    

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """

        # phone1=validated_data.get('phone_1')
        # access_token1=Register.objects.filter(phone=phone1).values('token_generated')

        # if(Register.objects.filter(phone=validated_data.get('phone_2')).exists()):
        #     phone2=validated_data.get('phone_2')
        #     access_token2=Register.objects.filter(phone=phone2).values('token_generated')


        #parse push notification
        # import json,httplib
        # connection = httplib.HTTPSConnection('api.parse.com', 443)
        # connection.connect()
        # connection.request('POST', '/1/installations', json.dumps({
        #        "deviceType": "ios",
        #        "pushType": "gcm",
        #        "deviceToken": "0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef",
        #        "GCMSenderId": "56712320625545",
        #        "channels": [
        #          "y3GamGlDf6K3CNW8cErPCl1VwysIWu"
        #        ]
        #      }), {
        #        "X-Parse-Application-Id": "ml4PVV8qbYzTys48zY8o9lSXXmHS4wuytKjgah8a",
        #        "X-Parse-REST-API-Key": "CAG8K4mUbZq3yDSpYiajKbWHcHZBhlh8QhS8te87",
        #        "Content-Type": "application/json"
        #      })
        # result = json.loads(connection.getresponse().read())
        # import sys
        # print >> sys.stderr, result

        # import json,httplib
        # connection = httplib.HTTPSConnection('api.parse.com', 443)
        # connection.connect()
        # connection.request('POST', '/1/push', json.dumps({
        #        "channels": [
        #          "y3GamGlDf6K3CNW8cErPCl1VwysIWu"
        #        ],
        #        "data": {
        #          "alert": "Your ticket has been reffered."
        #        }
        #      }), {
        #        "X-Parse-Application-Id": "ml4PVV8qbYzTys48zY8o9lSXXmHS4wuytKjgah8a",
        #        "X-Parse-REST-API-Key": "CAG8K4mUbZq3yDSpYiajKbWHcHZBhlh8QhS8te87",
        #        "Content-Type": "application/json"
        #      })
        # result = json.loads(connection.getresponse().read())
        # print >> sys.stderr, result
        
        import json
        return Connect.objects.create(connecter_vz_id=validated_data.get('connecter_vz_id'),phone_1=validated_data.get('phone_1'),ticket_id_1=validated_data.get('ticket_id_1'),phone_2=validated_data.get('phone_2'),ticket_id_2=validated_data.get('ticket_id_2'))
        #return validated_data


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

