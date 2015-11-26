from rest_framework import serializers
from connect.models import Connect, LANGUAGE_CHOICES, STYLE_CHOICES
from user_register.models import User_register, LANGUAGE_CHOICES, STYLE_CHOICES
from ticket_create.models import Ticket_create, LANGUAGE_CHOICES, STYLE_CHOICES



class ConnectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Connect
        fields = ('connecter_vz_id','phone_1', 'ticket_id_1', 'phone_2', 'ticket_id_2','my_ticket','reffered_ticket','reffered_phone')
    

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        
        import json
        Connect.objects.create(connecter_vz_id=validated_data.get('connecter_vz_id'),my_ticket=validated_data.get('ticket_id_1'),reffered_ticket=validated_data.get('ticket_id_2'),reffered_phone=validated_data.get('phone_2'))
        Connect.objects.create(connecter_vz_id=validated_data.get('connecter_vz_id'),my_ticket=validated_data.get('ticket_id_2'),reffered_ticket=validated_data.get('ticket_id_1'),reffered_phone=validated_data.get('phone_1'))
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

