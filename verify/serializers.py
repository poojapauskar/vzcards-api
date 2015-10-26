from rest_framework import serializers
from verify.models import Verify, LANGUAGE_CHOICES, STYLE_CHOICES

from register.models import Register, LANGUAGE_CHOICES, STYLE_CHOICES



class VerifySerializer(serializers.ModelSerializer):
    class Meta:
        model = Verify
        fields = ('phone','otp','valid')
    

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        from oauthlib.common import generate_token
        token = generate_token()
        

        if (Register.objects.filter(phone=validated_data.get('phone')).values('firstname')).exists():
    	 Verify.objects.filter(phone=validated_data.get('phone')).delete()

        if (Register.objects.filter(phone=validated_data.get('phone')).filter(otp_generated=validated_data.get('otp')).values('firstname')).exists():
         objects=Verify.objects.create(phone=validated_data.get('phone'),otp=validated_data.get('otp'),valid=1)
    	 #objects=validated_data	
            #Verify.objects.filter(phone=validated_data.get('phone')).update(valid=1)

        if (Register.objects.filter(phone=validated_data.get('phone')).filter(otp_generated=validated_data.get('otp')).values('firstname')).exists():
         Register.objects.filter(phone=validated_data.get('phone')).update(access_token=token)
        
    	else:
         objects=Verify.objects.create(phone=validated_data.get('phone'),otp=validated_data.get('otp'),valid=0)
		
        
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

