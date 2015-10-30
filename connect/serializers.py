from rest_framework import serializers
from connect.models import Connect, LANGUAGE_CHOICES, STYLE_CHOICES
from register.models import Register, LANGUAGE_CHOICES, STYLE_CHOICES



class ConnectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Connect
        fields = ('connecter_vz_id','connecter_details', 'phone_1', 'ticket_id_1', 'phone_2', 'ticket_id_2','ticket_1_details','ticket_2_details','phone_1_details','phone_2_details')
    

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        connecter_details=Register.objects.filter(vz_id=validated_data.get('connecter_vz_id')).values('token_generated','firstname', 'lastname', 'email', 'phone','vz_id','industry','company','address_line_1','address_line_2','city','pin_code','otp_generated')
        ticket_1_details=Ticket.objects.filter(ticket_id=ticket_id_1).values('vz_id','user_details', 'question', 'item', 'description','date_created','date_validity','ticket_id')
        ticket_2_details=Ticket.objects.filter(ticket_id=ticket_id_2).values('vz_id','user_details', 'question', 'item', 'description','date_created','date_validity','ticket_id')
        phone_1_details=Register.objects.filter(phone=validated_data.get('phone_1')).values('token_generated','firstname', 'lastname', 'email', 'phone','vz_id','industry','company','address_line_1','address_line_2','city','pin_code','otp_generated')
        phone_2_details=Register.objects.filter(phone=validated_data.get('phone_2')).values('token_generated','firstname', 'lastname', 'email', 'phone','vz_id','industry','company','address_line_1','address_line_2','city','pin_code','otp_generated')

        return Connect.objects.create(**validated_data)

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

