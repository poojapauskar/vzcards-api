from rest_framework import serializers
from sync_contacts.models import Sync_contacts, LANGUAGE_CHOICES, STYLE_CHOICES
from register.models import Register, LANGUAGE_CHOICES, STYLE_CHOICES
from django.db.models import Count

class Sync_contactsSerializer(serializers.ModelSerializer):
    class Meta:

    	model = Register
        fields = ('vz_id',)

        model = Sync_contacts
        fields = ('vz_id', 'contact_list','friends_vz_id')
    

    def create(self, validated_data):
        
        #convert array to string
        import json
        friends_list=list(Register.objects.filter(phone__in=validated_data.get('contact_list')).values_list('vz_id', flat=True))
        
        friends_list = json.dumps(friends_list)

        #friends_list=str(friends_list)[1:-1]
        
        #friends_list=str(friends_list).replace('[','').replace(']','').replace("'","")
        # friends_list=friends_list.replace("(","")
        # friends_list=friends_list.replace(")","")
        # friends_list=friends_list.replace("'","")
        #friends_list=friends_list.replace('"','')

        import sys
        print >> sys.stderr, friends_list
       

        Sync_contacts.objects.filter(vz_id=validated_data.get('vz_id')).delete()
        objects=Sync_contacts.objects.create(vz_id=validated_data.get('vz_id'),contact_list=validated_data.get('contact_list'),friends_vz_id=friends_list)
        

        #print >> sys.stderr, objects.query
       
        return objects


    def update(self, instance, validated_data):
        
        instance.vz_id = validated_data.get('vz_id', instance.vz_id)
        instance.contact_list = validated_data.get('contact_list', instance.contact_list)
        instance.friends_vz_id = validated_data.get('friends_vz_id', instance.friends_vz_id)
        instance.save()
        return instance

from sync_contacts.models import Sync_contacts
from sync_contacts.serializers import Sync_contactsSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser




from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    sync_contacts = serializers.PrimaryKeyRelatedField(many=True, queryset=Sync_contacts.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'sync_contacts')

owner = serializers.ReadOnlyField(source='owner.username')

