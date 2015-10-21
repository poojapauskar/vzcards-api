from rest_framework import serializers
from friends.models import Friends, LANGUAGE_CHOICES, STYLE_CHOICES



class FriendsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friends
        fields = ('vz_id', 'friends_vz_id')
    


from friends.models import Friends
from friends.serializers import FriendsSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser




from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    friends = serializers.PrimaryKeyRelatedField(many=True, queryset=Friends.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'friends')

owner = serializers.ReadOnlyField(source='owner.username')

