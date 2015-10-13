from register.models import Register
from send_again.serializers import Send_againSerializer
from rest_framework import generics
# from send_again.permissions import IsOwnerOrReadOnly
# from rest_framework import permissions


class Send_againList(generics.ListCreateAPIView):
 queryset = Register.objects.all()
 serializer_class = Send_againSerializer
 # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)



class Send_againDetail(generics.RetrieveUpdateDestroyAPIView):
 queryset = Register.objects.all()
 serializer_class = Send_againSerializer
 # permission_classes = (permissions.IsAuthenticatedOrReadOnly,
 #                      IsOwnerOrReadOnly,)


from django.contrib.auth.models import User
from send_again.serializers import UserSerializer
from rest_framework import permissions


class UserList(generics.ListAPIView):
 queryset = User.objects.all()
 serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
 queryset = User.objects.all()
 serializer_class = UserSerializer


def perform_create(self, serializer):
 serializer.save(owner=self.request.user)




