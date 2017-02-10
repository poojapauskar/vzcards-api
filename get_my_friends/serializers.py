from rest_framework import serializers
from ticket_create.models import Ticket_create, LANGUAGE_CHOICES, STYLE_CHOICES
from friends.models import Friends, LANGUAGE_CHOICES, STYLE_CHOICES
from sync.models import Sync, LANGUAGE_CHOICES, STYLE_CHOICES
from user_register.models import User_register, LANGUAGE_CHOICES, STYLE_CHOICES



class Get_my_friendsSerializer(serializers.ModelSerializer):
    class Meta:

        # model = Friends
        # fields = ('vz_id','friends_vz_id',)

    	model = Sync
    	fields = ('friends_vz_id',)
        
        model = User_register
        fields = ('pk', 'firstname','company_photo', 'lastname','title', 'email', 'phone','vz_id','industry','company','address_line_1','address_line_2','city','pin_code','photo')
       
        


    from ticket_create.models import Ticket_create
from get_my_friends.serializers import Get_my_friendsSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser




from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    create = serializers.PrimaryKeyRelatedField(many=True, queryset=Ticket_create.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'create')

owner = serializers.ReadOnlyField(source='owner.username')

