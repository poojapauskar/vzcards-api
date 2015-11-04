from rest_framework import serializers
from api.models import Api, LANGUAGE_CHOICES, STYLE_CHOICES



class ApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Api
        fields = ('vzcards','register','verify','send_again','sync', 'my_profile','my_profile_update','get_my_friends','get_list', 'get_my_tickets','connect','ticket_create','ticket_details','response','reffered','upload_image')
    

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """

        Api.objects.all().delete()
        return Api.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.vzcards = validated_data.get('vzcards', instance.vzcards)
        instance.register = validated_data.get('register', instance.register)
        instance.verify = validated_data.get('verify', instance.verify)
        instance.send_again = validated_data.get('send_again', instance.send_again)
        instance.sync = validated_data.get('sync', instance.sync)
        instance.my_profile = validated_data.get('my_profile', instance.my_profile)
        instance.my_profile_update = validated_data.get('my_profile', instance.my_profile_update)
        instance.get_my_friends = validated_data.get('get_my_friends', instance.get_my_friends)
        instance.get_list = validated_data.get('get_list', instance.get_list)
        instance.get_my_tickets = validated_data.get('get_my_tickets', instance.get_my_tickets)
        instance.connect = validated_data.get('connect', instance.connect)
        instance.ticket_create= validated_data.get('ticket_create', instance.ticket_create)
        instance.ticket_details = validated_data.get('ticket_details', instance.ticket_details)
        instance.response = validated_data.get('response', instance.response)
        instance.reffered = validated_data.get('reffered', instance.reffered)
        instance.upload_image = validated_data.get('upload_image', instance.upload_image)
        
        instance.save()
        return instance


    from api.models import Api
from api.serializers import ApiSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser



from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    connect = serializers.PrimaryKeyRelatedField(many=True, queryset=Api.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'connect')

owner = serializers.ReadOnlyField(source='owner.username')

