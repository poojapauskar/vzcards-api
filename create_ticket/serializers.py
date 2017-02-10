from rest_framework import serializers
from create_ticket.models import Create_ticket, LANGUAGE_CHOICES, STYLE_CHOICES
from register.models import Register, LANGUAGE_CHOICES, STYLE_CHOICES

import random
from random import randint



class Create_ticketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Create_ticket
        fields = ('access_token','vz_id','user_details', 'question', 'item', 'description','date_created','date_validity','ticket_id')
    

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """

        vz_id=Register.objects.filter(access_token=validated_data.get('access_token')).values('vz_id')[0]
        ticket_id=str(random.randint(100000, 999999))
        user_details= Register.objects.filter(vz_id=vz_id).values('firstname','lastname','email','phone')
        return Create_ticket.objects.create(access_token=validated_data.get('access_token'),vz_id=vz_id,user_details=user_details,question=validated_data.get('question'),item=validated_data.get('item'),description=validated_data.get('description'),date_validity=validated_data.get('date_validity'),ticket_id=ticket_id)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.access_token = validated_data.get('access_token', instance.access_token)
        instance.vz_id = validated_data.get('vz_id', instance.vz_id)
        instance.user_details = validated_data.get('user_details', instance.user_details)
        instance.question = validated_data.get('question', instance.question)
        instance.item = validated_data.get('item', instance.item)
        instance.description = validated_data.get('description', instance.description)
        instance.date_created = validated_data.get('date_created', instance.date_created)
        instance.date_validity = validated_data.get('date_validity', instance.date_validity)
        instance.ticket_id = validated_data.get('ticket_id', instance.ticket_id)
        instance.save()
        return instance

        


    from create_ticket.models import Create_ticket
from create_ticket.serializers import Create_ticketSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser



from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    create = serializers.PrimaryKeyRelatedField(many=True, queryset=Create_ticket.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'create')

owner = serializers.ReadOnlyField(source='owner.username')

