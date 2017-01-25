from rest_framework import serializers
from verify.models import Verify, LANGUAGE_CHOICES, STYLE_CHOICES

from user_register.models import User_register, LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth.models import User, Group



class VerifySerializer(serializers.ModelSerializer):
    class Meta:

        model = User

        model = Verify
        fields = ('phone','otp','valid','token_generated','vz_id')
    

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """

        objects=Verify.objects.create(phone=validated_data.get('phone'),otp=validated_data.get('otp'),valid=validated_data.get('valid'),token_generated=validated_data.get('token_generated'),vz_id=validated_data.get('vz_id'))

        # from django.shortcuts import render_to_response
        # return render_to_response(token, status=200)
 
        return objects

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.phone = validated_data.get('phone', instance.phone)
        instance.otp = validated_data.get('otp', instance.otp)
        instance.valid = validated_data.get('valid', instance.valid)
        return instance

        


    from verify.models import Verify
from verify.serializers import VerifySerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser



from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    create = serializers.PrimaryKeyRelatedField(many=True, queryset=Verify.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'create')

owner = serializers.ReadOnlyField(source='owner.username')

