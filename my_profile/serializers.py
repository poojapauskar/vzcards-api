from rest_framework import serializers
from register.models import Register, LANGUAGE_CHOICES, STYLE_CHOICES



class My_profileSerializer(serializers.ModelSerializer):
    class Meta:

        model = Register
        fields = ('firstname','lastname','email','industry','address_line_1','address_line_2','city','pin_code')
        
    # def create(self, validated_data): 
 	  # vz_id = self.kwargs['vz_id']

 	  #    # if (validated_data.get('firstname') != ''):
    #    #   	objects=Register.objects.filter(vz_id=vz_id).update(firstname=validated_data.get('firstname'))
    #    #  if (validated_data.get('lastname') != ''):
    #    #   	objects=Register.objects.filter(vz_id=vz_id).update(lastname=validated_data.get('lastname'))
    #    #  if (validated_data.get('email') != ''):
    #    #   	objects=Register.objects.filter(vz_id=vz_id).update(email=validated_data.get('email'))
    #    #  if (validated_data.get('industry') != ''):
    #    #   	objects=Register.objects.filter(vz_id=vz_id).update(industry=validated_data.get('industry'))
    #    #  if (validated_data.get('address_line_1') != ''):
    #    #   	objects=Register.objects.filter(vz_id=vz_id).update(address_line_1=validated_data.get('address_line_1'))
    #    #  if (validated_data.get('address_line_2') != ''):
    #    #   	objects=Register.objects.filter(vz_id=vz_id).update(address_line_2=validated_data.get('address_line_2'))
    #    #  if (validated_data.get('city') != ''):
    #    #   	objects=Register.objects.filter(vz_id=vz_id).update(city=validated_data.get('city'))
    #    #  if (validated_data.get('pin_code') != ''):
    #    #   	objects=Register.objects.filter(vz_id=vz_id).update(pin_code=validated_data.get('pin_code'))


    #  Register.objects.filter(vz_id=vz_id).update(firstname=validated_data.get('firstname'),lastname=validated_data.get('lastname'),email=validated_data.get('email'),industry=validated_data.get('industry'),address_line_1=validated_data.get('address_line_1'),address_line_2=validated_data.get('address_line_2'),city=validated_data.get('city'),pin_code=validated_data.get('pin_code'))
    #return validated_data

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.firstname = validated_data.get('firstname', instance.firstname)
        instance.lastname = validated_data.get('lastname', instance.lastname)
        instance.email = validated_data.get('email', instance.email)
        instance.vz_id = validated_data.get('vz_id', instance.vz_id)
        instance.industry = validated_data.get('industry', instance.industry)
        instance.address_line_1 = validated_data.get('address_line_1', instance.address_line_1)
        instance.address_line_2 = validated_data.get('address_line_2', instance.address_line_2)
        instance.city = validated_data.get('city', instance.city)
        instance.pin_code = validated_data.get('pin_code', instance.pin_codes)
        instance.save()
        return instance

from ticket.models import Ticket
from my_profile.serializers import My_profileSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser




from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    create = serializers.PrimaryKeyRelatedField(many=True, queryset=Register.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'create')

owner = serializers.ReadOnlyField(source='owner.username')

