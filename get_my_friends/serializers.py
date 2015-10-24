from rest_framework import serializers
from ticket.models import Ticket, LANGUAGE_CHOICES, STYLE_CHOICES
from friends.models import Friends, LANGUAGE_CHOICES, STYLE_CHOICES
from sync.models import Sync, LANGUAGE_CHOICES, STYLE_CHOICES
from register.models import Register, LANGUAGE_CHOICES, STYLE_CHOICES



class Get_my_friendsSerializer(serializers.ModelSerializer):
    class Meta:

        # model = Friends
        # fields = ('vz_id','friends_vz_id',)

    	model = Sync
    	fields = ('friends_vz_id',)
        
        model = Register
        fields = ('pk', 'firstname', 'lastname', 'email', 'phone','vz_id','industry','company','address_line_1','address_line_2','city','pin_code')
       
        


    from ticket.models import Ticket
from get_my_friends.serializers import Get_my_friendsSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser




from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    create = serializers.PrimaryKeyRelatedField(many=True, queryset=Ticket.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'create')

owner = serializers.ReadOnlyField(source='owner.username')

