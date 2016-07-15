from ticket_create.models import Ticket_create
from upload_image.models import Upload_image
from connect.models import Connect
from remove_ticket.serializers import Remove_ticketSerializer
from rest_framework import generics

# from ticket.permissions import IsOwnerOrReadOnly
# from rest_framework import permissions
from django.shortcuts import get_object_or_404

from django.http import JsonResponse

import cloudinary
import cloudinary.uploader
import cloudinary.api


cloudinary.config( 
  cloud_name = "harnesymz", 
  api_key = "597912151168824", 
  api_secret = "u1Dgxp3BDnIgm-PN_gkJ5stDE30" 
)

class Remove_ticketDetail(generics.ListAPIView):
 serializer_class = Remove_ticketSerializer


 def get_queryset(self):
  ticket_id = self.kwargs['ticket_id']

  objects1=Ticket_create.objects.filter(ticket_id=ticket_id)

  if(Ticket_create.objects.filter(ticket_id=ticket_id).values_list('item_photo').exists()):
    #delete from cloudinary
    item_photo_1=Ticket_create.objects.filter(ticket_id=ticket_id).values_list('item_photo')
    import sys
    item_photo_2= str(item_photo_1[0]).replace("http://res.cloudinary.com/harnesymz/image/upload/","").replace(".jpg","").replace(",","").replace("u","").replace("'","").replace("(","").replace(")","")
    print sys.stderr, item_photo_2
    cloudinary.api.delete_resources([item_photo_2])
    #delete from upload image api
    item_photo_3 = (str(item_photo_2).replace("vzcards/","").replace(".jpg",""))+".jpg"
    print sys.stderr,item_photo_3
    Upload_image.objects.filter(link=item_photo_3).delete()

  objects=Ticket_create.objects.filter(ticket_id=ticket_id).delete()
  objects3=(Connect.objects.filter(ticket_id_1=ticket_id)|Connect.objects.filter(ticket_id_2=ticket_id)).delete()

  
  return objects1


       

from django.contrib.auth.models import User
from remove_ticket.serializers import UserSerializer
from rest_framework import permissions


class UserList(generics.ListAPIView):
 queryset = User.objects.all()
 serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
 queryset = User.objects.all()
 serializer_class = UserSerializer


def perform_create(self, serializer):
 serializer.save(owner=self.request.user)




from django.shortcuts import render

# Create your views here.
