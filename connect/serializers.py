from rest_framework import serializers
from connect.models import Connect, LANGUAGE_CHOICES, STYLE_CHOICES
from register.models import Register, LANGUAGE_CHOICES, STYLE_CHOICES
from ticket_create.models import Ticket_create, LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth.models import User, Group



class ConnectSerializer(serializers.ModelSerializer):
    class Meta:
        model = User

        model = Connect
        fields = ('connecter_vz_id','phone_1', 'ticket_id_1', 'phone_2', 'ticket_id_2')
    

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """

        # import zeropush

        # # Get a user. Can also be a custom user model in django 1.5+
        # the_user = User.objects.filter(access_token="THVIz2upMQyBrF7R4b894jU7RCVJmz")
        # zeropush.notify_user(the_user, alert="Here's some notification text", sound="default", badge_number=1)



        import json
        return Connect.objects.create(connecter_vz_id=validated_data.get('connecter_vz_id'),phone_1=validated_data.get('phone_1'),ticket_id_1=validated_data.get('ticket_id_1'),phone_2=validated_data.get('phone_2'),ticket_id_2=validated_data.get('ticket_id_2'))
        #return validated_data

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.connecter_vz_id = validated_data.get('connecter_vz_id', instance.connecter_vz_id)
        instance.phone_1 = validated_data.get('phone_1', instance.phone_1)
        instance.ticket_id_1 = validated_data.get('ticket_id_1', instance.ticket_id_1)
        instance.phone_2 = validated_data.get('phone_2', instance.phone_2)
        instance.ticket_id_2 = validated_data.get('ticket_id_2', instance.ticket_id_2)
        # instance.connecter_details = validated_data.get('connecter_details', instance.connecter_details)
        # instance.ticket_1_details = validated_data.get('ticket_1_details', instance.ticket_1_details)
        # instance.ticket_2_details = validated_data.get('ticket_2_details', instance.ticket_2_details)
        # instance.phone_1_details = validated_data.get('phone_1_details', instance.phone_1_details)
        # instance.phone_2_details = validated_data.get('phone_2_details', instance.phone_2_details)
        instance.save()
        return instance


    from connect.models import Connect
from connect.serializers import ConnectSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser



from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    connect = serializers.PrimaryKeyRelatedField(many=True, queryset=Connect.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'connect')

owner = serializers.ReadOnlyField(source='owner.username')

