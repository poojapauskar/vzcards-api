from rest_framework import serializers
from connect.models import Connect, LANGUAGE_CHOICES, STYLE_CHOICES
from register.models import Register, LANGUAGE_CHOICES, STYLE_CHOICES
from ticket_create.models import Ticket_create, LANGUAGE_CHOICES, STYLE_CHOICES



class ConnectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Connect
        fields = ('connecter_vz_id','connecter_details', 'phone_1', 'ticket_id_1', 'phone_2', 'ticket_id_2','ticket_1_details','ticket_2_details','phone_1_details','phone_2_details','ticket_1_dates','ticket_2_dates')
    

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        #import json
        connecter_details=list(Register.objects.filter(vz_id=validated_data.get('connecter_vz_id')).values_list('token_generated','firstname', 'lastname', 'email', 'phone','vz_id','industry','company','address_line_1','address_line_2','city','pin_code','otp_generated','photo'))
        ticket_1_details=list(Ticket_create.objects.filter(ticket_id=validated_data.get('ticket_id_1')).values_list('vz_id','question', 'item', 'description','ticket_id','item_photo'))
        ticket_2_details=list(Ticket_create.objects.filter(ticket_id=validated_data.get('ticket_id_2')).values_list('vz_id','question', 'item', 'description','ticket_id','item_photo'))
        phone_1_details=list(Register.objects.filter(phone=validated_data.get('phone_1')).values_list('token_generated','firstname', 'lastname', 'email', 'phone','vz_id','industry','company','address_line_1','address_line_2','city','pin_code','otp_generated','photo'))
        phone_2_details=list(Register.objects.filter(phone=validated_data.get('phone_2')).values_list('token_generated','firstname', 'lastname', 'email', 'phone','vz_id','industry','company','address_line_1','address_line_2','city','pin_code','otp_generated','photo'))
        ticket_1_dates=list(Ticket_create.objects.filter(ticket_id=validated_data.get('ticket_id_1')).values_list('date_validity'))
        ticket_2_dates=list(Ticket_create.objects.filter(ticket_id=validated_data.get('ticket_id_1')).values_list('date_validity'))
        
        #import bson
        #from bson import json_util
        import json

#json.dumps(anObject, default=json_util.default)

        connecter_details = json.dumps(connecter_details)
        ticket_1_details = json.dumps(ticket_1_details)
        ticket_2_details = json.dumps(ticket_2_details)
        phone_1_details = json.dumps(phone_1_details)
        phone_2_details = json.dumps(phone_2_details)

        ticket_1_details=ticket_1_details.replace('"','').replace(']','').replace('[','')
        ticket_2_details=ticket_2_details.replace('"','').replace(']','').replace('[','')
        connecter_details=connecter_details.replace('"','').replace(']','').replace('[','')
        phone_1_details=phone_1_details.replace('"','').replace(']','').replace('[','')
        phone_2_details=phone_2_details.replace('"','').replace(']','').replace('[','')

        return Connect.objects.create(connecter_vz_id=validated_data.get('connecter_vz_id'),connecter_details=connecter_details,phone_1=validated_data.get('phone_1'),ticket_id_1=validated_data.get('ticket_id_1'),phone_2=validated_data.get('phone_2'),ticket_id_2=validated_data.get('ticket_id_2'),ticket_1_details=ticket_1_details,ticket_2_details=ticket_2_details,phone_1_details=phone_1_details,phone_2_details=phone_2_details,ticket_1_dates=ticket_1_dates,ticket_2_dates=ticket_2_dates)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.connecter_vz_id = validated_data.get('connecter_vz_id', instance.connecter_vz_id)
        instance.phone_1 = validated_data.get('phone_1', instance.phone_1)
        instance.ticket_id_1 = validated_data.get('ticket_id_1', instance.ticket_id_1)
        instance.phone_2 = validated_data.get('phone_2', instance.phone_2)
        instance.ticket_id_2 = validated_data.get('ticket_id_2', instance.ticket_id_2)
        instance.connecter_details = validated_data.get('connecter_details', instance.connecter_details)
        instance.ticket_1_details = validated_data.get('ticket_1_details', instance.ticket_1_details)
        instance.ticket_2_details = validated_data.get('ticket_2_details', instance.ticket_2_details)
        instance.phone_1_details = validated_data.get('phone_1_details', instance.phone_1_details)
        instance.phone_2_details = validated_data.get('phone_2_details', instance.phone_2_details)
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

