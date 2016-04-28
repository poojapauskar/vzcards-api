from rest_framework import serializers
from sync.models import Sync, LANGUAGE_CHOICES, STYLE_CHOICES
from user_register.models import User_register, LANGUAGE_CHOICES, STYLE_CHOICES
from django.db.models import Count

class SyncSerializer(serializers.ModelSerializer):
    class Meta:

    	model = User_register
        fields = ('vz_id',)

        model = Sync
        fields = ('vz_id', 'contact_list','friends_vz_id')
    

    def create(self, validated_data):
        
        #convert array to string
        import json
        print >> sys.stderr, validated_data.get('contact_list')
        
        friends_list=list(User_register.objects.filter(phone__in=validated_data.get('contact_list')).values_list('vz_id', flat=True))
        
        friends_list = json.dumps(friends_list)

        #friends_list=str(friends_list)[1:-1]
        
        #friends_list=str(friends_list).replace('[','').replace(']','').replace("'","")
        # friends_list=friends_list.replace("(","")
        # friends_list=friends_list.replace(")","")
        # friends_list=friends_list.replace("'","")
        #friends_list=friends_list.replace('"','')

        import sys
        print >> sys.stderr, friends_list
       

        Sync.objects.filter(vz_id=validated_data.get('vz_id')).delete()
        objects=Sync.objects.create(vz_id=validated_data.get('vz_id'),contact_list=validated_data.get('contact_list'),friends_vz_id=friends_list)
        

        #print >> sys.stderr, objects.query
       
        return objects


    def update(self, instance, validated_data):
        
        instance.vz_id = validated_data.get('vz_id', instance.vz_id)
        instance.contact_list = validated_data.get('contact_list', instance.contact_list)
        instance.friends_vz_id = validated_data.get('friends_vz_id', instance.friends_vz_id)
        instance.save()
        return instance

from sync.models import Sync
from sync.serializers import SyncSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser




from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    sync = serializers.PrimaryKeyRelatedField(many=True, queryset=Sync.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'sync')

owner = serializers.ReadOnlyField(source='owner.username')

