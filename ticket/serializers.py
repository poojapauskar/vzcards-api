from rest_framework import serializers
from ticket.models import Ticket, LANGUAGE_CHOICES, STYLE_CHOICES
from register.models import Register, LANGUAGE_CHOICES, STYLE_CHOICES

import random
from random import randint



class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ('vz_id','user_details', 'question', 'item', 'description','date_created','date_validity','ticket_id')
    

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        ticket_id=str(random.randint(100000, 999999))
        
        #Ticket.objects.all().delete()
        import json
        user_details= list(Register.objects.filter(vz_id=validated_data.get('vz_id')).values_list('firstname','lastname','email','phone','token_generated','vz_id','industry','company','address_line_1','address_line_2','city','pin_code','otp_generated'))
        user_details = json.dumps(user_details)
        user_details=str(user_details).replace('"','').replace(']','').replace('[','')
        #print >> sys.stderr, user_details
        #user_details= user_details.split()
        #Ticket.objects.all().delete()
        return Ticket.objects.create(vz_id=validated_data.get('vz_id'),user_details=user_details,question=validated_data.get('question'),item=validated_data.get('item'),description=validated_data.get('description'),date_validity=validated_data.get('date_validity'),ticket_id=ticket_id)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
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

        


    from ticket.models import Ticket
from ticket.serializers import TicketSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser



from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    create = serializers.PrimaryKeyRelatedField(many=True, queryset=Ticket.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'create')

owner = serializers.ReadOnlyField(source='owner.username')

