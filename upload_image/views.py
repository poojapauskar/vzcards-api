from upload_image.models import Upload_image
from upload_image.serializers import Upload_imageSerializer
from rest_framework import generics
# from upload_image.permissions import IsOwnerOrReadOnly
# from rest_framework import permissions


class Upload_imageList(generics.ListCreateAPIView):
 queryset = Upload_image.objects.all()
 serializer_class = Upload_imageSerializer
 # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)



class Upload_imageDetail(generics.RetrieveUpdateDestroyAPIView):
 queryset = Upload_image.objects.all()
 serializer_class = Upload_imageSerializer
 # permission_classes = (permissions.IsAuthenticatedOrReadOnly,
 #                      IsOwnerOrReadOnly,)


from django.contrib.auth.models import User
from upload_image.serializers import UserSerializer
from rest_framework import permissions


class UserList(generics.ListAPIView):
 queryset = User.objects.all()
 serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
 queryset = User.objects.all()
 serializer_class = UserSerializer


def perform_create(self, serializer):
 serializer.save(owner=self.request.user)




