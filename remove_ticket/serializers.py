from rest_framework import serializers
from ticket_create.models import Ticket_create, LANGUAGE_CHOICES, STYLE_CHOICES




class Remove_ticketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket_create
        fields = ('vz_id','item_photo','question', 'item', 'description','date_created','date_validity','ticket_id')
    
    

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.vz_id = validated_data.get('vz_id', instance.vz_id)
        instance.user_details = validated_data.get('user_details', instance.user_details)
        instance.question = validated_data.get('question', instance.question)
        instance.item_photo = validated_data.get('item_photo', instance.item_photo)
        instance.item = validated_data.get('item', instance.item)
        instance.description = validated_data.get('description', instance.description)
        instance.date_created = validated_data.get('date_created', instance.date_created)
        instance.date_validity = validated_data.get('date_validity', instance.date_validity)
        instance.ticket_id = validated_data.get('ticket_id', instance.ticket_id)
        instance.save()
        return instance

from ticket_create.models import Ticket_create
from remove_ticket.serializers import Remove_ticketSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser




from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    create = serializers.PrimaryKeyRelatedField(many=True, queryset=Ticket_create.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'create')

owner = serializers.ReadOnlyField(source='owner.username')

