from rest_framework import serializers
from ticket.models import Ticket, LANGUAGE_CHOICES, STYLE_CHOICES



class Get_my_ticketsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ('vz_id', 'question', 'item', 'description', 'cost','date_created','date_validity')
    	


    from ticket.models import Ticket
from get_my_tickets.serializers import Get_my_ticketsSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser




from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    create = serializers.PrimaryKeyRelatedField(many=True, queryset=Ticket.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'get_my_tickets')

owner = serializers.ReadOnlyField(source='owner.username')

