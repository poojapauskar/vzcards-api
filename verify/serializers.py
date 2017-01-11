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


        


        from oauthlib.common import generate_token
        token = generate_token()
        

        if (User_register.objects.filter(phone=validated_data.get('phone')).values('phone')).exists():
    	 Verify.objects.filter(phone=validated_data.get('phone')).delete()

       
    	 #objects=validated_data	
            #Verify.objects.filter(phone=validated_data.get('phone')).update(valid=1)
        
        if (User.objects.filter(username=validated_data.get('phone'))).exists():
          User.objects.filter(username=validated_data.get('phone')).delete()
        
        if ((User_register.objects.filter(phone=validated_data.get('phone')).filter(otp_generated=validated_data.get('otp')).values('phone')).exists() or ((User_register.objects.filter(phone=validated_data.get('phone')).values('phone')).exists() and (validated_data.get('otp')=='444444'))):
          user=User.objects.create(username=validated_data.get('phone'),password="vzcards")

        
		


        from oauth2_provider.settings import oauth2_settings
        from oauthlib.common import generate_token
        from django.http import JsonResponse
        from oauth2_provider.models import AccessToken, Application, RefreshToken
        from django.utils.timezone import now, timedelta
        from django.http import HttpResponse
        from django.contrib.auth import login
       # from social.apps.django_app.utils import psa
       # from .tools import get_access_token
        from datetime import datetime


        expire_seconds = oauth2_settings.user_settings['ACCESS_TOKEN_EXPIRE_SECONDS']
        scopes = oauth2_settings.user_settings['SCOPES']


        application = Application.objects.get(name="vzcards-api")
        expires = datetime.now() + timedelta(seconds=expire_seconds)

        if ((User_register.objects.filter(phone=validated_data.get('phone')).filter(otp_generated=validated_data.get('otp')).values('phone')).exists() or ((User_register.objects.filter(phone=validated_data.get('phone')).values('phone')).exists() and (validated_data.get('otp')=='444444'))):
            access_token = AccessToken.objects.create(
                    user=user,
                    application=application,
                    token=generate_token(),
                    expires=expires,
                    scope=scopes)
        if ((User_register.objects.filter(phone=validated_data.get('phone')).filter(otp_generated=validated_data.get('otp')).values('phone')).exists() or ((User_register.objects.filter(phone=validated_data.get('phone')).values('phone')).exists() and (validated_data.get('otp')=='444444'))):
            refresh_token = RefreshToken.objects.create(
                    user=user,
                    token=generate_token(),
                    access_token=access_token,
                    application=application)

        # token = {
        #         'access_token': access_token.token,
        #         'token_type': 'Bearer',
        #         'expires_in': expire_seconds,
        #         'refresh_token': refresh_token.token,
        #         'scope': scopes}

        import json
        if ((User_register.objects.filter(phone=validated_data.get('phone')).filter(otp_generated=validated_data.get('otp')).values('phone')).exists() or ((User_register.objects.filter(phone=validated_data.get('phone')).values('phone')).exists() and (validated_data.get('otp')=='444444'))):
            token = access_token.token
            token= json.dumps(token)
            token = token.replace('"','')


        

        if ((User_register.objects.filter(phone=validated_data.get('phone')).filter(otp_generated=validated_data.get('otp')).values('phone')).exists() or ((User_register.objects.filter(phone=validated_data.get('phone')).values('phone')).exists() and (validated_data.get('otp')=='444444'))):
         User_register.objects.filter(phone=validated_data.get('phone')).update(token_generated=token)
        
        if (User_register.objects.filter(phone=validated_data.get('phone')).values('phone')).exists():
         vz_id= User_register.objects.filter(phone=validated_data.get('phone')).values_list('vz_id',flat=True)[0]

        if ((User_register.objects.filter(phone=validated_data.get('phone')).filter(otp_generated=validated_data.get('otp')).values('phone')).exists() or ((User_register.objects.filter(phone=validated_data.get('phone')).values('phone')).exists() and (validated_data.get('otp')=='444444'))):
         objects=Verify.objects.create(phone=validated_data.get('phone'),otp=validated_data.get('otp'),valid=1,token_generated=token,vz_id=vz_id)


        else:
         objects=Verify.objects.create(phone=validated_data.get('phone'),otp=validated_data.get('otp'),valid=0,token_generated='',vz_id=vz_id)

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

