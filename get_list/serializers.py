from rest_framework import serializers
from ticket.models import Ticket, LANGUAGE_CHOICES, STYLE_CHOICES
from friends.models import Friends, LANGUAGE_CHOICES, STYLE_CHOICES
from sync_contacts.models import Sync_contacts, LANGUAGE_CHOICES, STYLE_CHOICES
from register.models import Register, LANGUAGE_CHOICES, STYLE_CHOICES



class Get_listSerializer(serializers.ModelSerializer):
    class Meta:

        # model = Friends
        # fields = ('vz_id','friends_vz_id',)

    	model = Sync_contacts
    	fields = ('friends_vz_id',)
        
        # model = Ticket
        # fields = ('user_details','question', 'item', 'description','date_created','date_validity','ticket_id','vz_id')
        
        


    from ticket.models import Ticket
from get_list.serializers import Get_listSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser




from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    create = serializers.PrimaryKeyRelatedField(many=True, queryset=Ticket.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'create')

owner = serializers.ReadOnlyField(source='owner.username')

