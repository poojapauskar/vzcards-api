from verify.models import Verify
from verify.serializers import VerifySerializer
from rest_framework import generics
# from verify.permissions import IsOwnerOrReadOnly
# from rest_framework import permissions


class VerifyList(generics.ListCreateAPIView):
 queryset = Verify.objects.all()
 serializer_class = VerifySerializer
 # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)



class VerifyDetail(generics.RetrieveUpdateDestroyAPIView):
 queryset = Verify.objects.all()
 serializer_class = VerifySerializer
 # permission_classes = (permissions.IsAuthenticatedOrReadOnly,
 #                      IsOwnerOrReadOnly,)


from django.contrib.auth.models import User
from create_object.serializers import UserSerializer
from rest_framework import permissions


class UserList(generics.ListAPIView):
 queryset = User.objects.all()
 serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
 queryset = User.objects.all()
 serializer_class = UserSerializer


def perform_create(self, serializer):
 serializer.save(owner=self.request.user)




