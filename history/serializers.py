from rest_framework import serializers
from connect.models import Connect, LANGUAGE_CHOICES, STYLE_CHOICES
from user_register.models import User_register, LANGUAGE_CHOICES, STYLE_CHOICES
from ticket_create.models import Ticket_create, LANGUAGE_CHOICES, STYLE_CHOICES




class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = User_register
        fields = ('phone','company_photo','photo','firstname', 'lastname', 'title','email','vz_id','industry','company','address_line_1','address_line_2','city','pin_code')

        model = Connect
        fields = ('connecter_vz_id', 'phone_1', 'ticket_id_1', 'phone_2', 'ticket_id_2')
        
        model = Ticket_create
        fields = ('vz_id','item_photo','user_details', 'question', 'item', 'description','date_created','date_validity','ticket_id')
    
    

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.connecter_vz_id = validated_data.get('connecter_vz_id', instance.connecter_vz_id)
        instance.phone_1 = validated_data.get('phone_1', instance.phone_1)
        instance.ticket_id_1 = validated_data.get('ticket_id_1', instance.ticket_id_1)
        instance.phone_2 = validated_data.get('phone_2', instance.phone_2)
        instance.ticket_id_2 = validated_data.get('ticket_id_2', instance.ticket_id_2)
        instance.save()
        return instance

from ticket_create.models import Ticket_create
from history.serializers import HistorySerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser




from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    create = serializers.PrimaryKeyRelatedField(many=True, queryset=User_register.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'create')

owner = serializers.ReadOnlyField(source='owner.username')

