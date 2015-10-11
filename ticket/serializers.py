from rest_framework import serializers
from ticket.models import Ticket, LANGUAGE_CHOICES, STYLE_CHOICES



class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ('vz_id', 'question', 'item', 'description', 'cost','date_created','date_validity','ticket_id')
    

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Ticket.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.vz_id = validated_data.get('vz_id', instance.vz_id)
        instance.question = validated_data.get('question', instance.question)
        instance.item = validated_data.get('item', instance.item)
        instance.description = validated_data.get('description', instance.description)
        instance.cost = validated_data.get('cost', instance.cost)
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

