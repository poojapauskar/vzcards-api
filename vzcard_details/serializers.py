from rest_framework import serializers
from ticket_create.models import Ticket_create, LANGUAGE_CHOICES, STYLE_CHOICES
from friends.models import Friends, LANGUAGE_CHOICES, STYLE_CHOICES
from sync.models import Sync, LANGUAGE_CHOICES, STYLE_CHOICES
from user_register.models import User_register, LANGUAGE_CHOICES, STYLE_CHOICES



class Vzcard_detailsSerializer(serializers.ModelSerializer):
    class Meta:

        # model = Friends
        # fields = ('vz_id','friends_vz_id',)
        # model = Register
        # fields = ('',)
        

    	model = User_register
    	fields = ('pk','token_generated','company_photo','photo','firstname', 'lastname', 'email', 'phone','vz_id','industry','company','address_line_1','address_line_2','city','pin_code','otp_generated')
        
        # model = Ticket
        # fields = ('user_details','question', 'item', 'description','date_created','date_validity','ticket_id','vz_id')
        
        


    from ticket_create.models import Ticket_create
from vzcard_details.serializers import Vzcard_detailsSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser




from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    create = serializers.PrimaryKeyRelatedField(many=True, queryset=Ticket_create.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'create')

owner = serializers.ReadOnlyField(source='owner.username')

