from connect.models import Connect
from register.models import Register
from ticket_create.models import Ticket_create
from history.serializers import HistorySerializer
from rest_framework import generics
# from ticket.permissions import IsOwnerOrReadOnly
# from rest_framework import permissions
from django.shortcuts import get_object_or_404

from django.http import JsonResponse

class StatusCode(object):
    OK = 200
    NOT_FOUND = 404
    # add more status code according to your need
import json
from django.http import HttpResponse
 
def JSONResponse(data = None, status = StatusCode.OK):
    if data is None:
        return HttpResponse(status)
    if data and type(data) is dict:
        return HttpResponse(json.dumps(data, indent = 4, encoding = 'utf-8', sort_keys = True), \
            mimetype = 'application/json', status = status)
    else:
        return HttpResponse(status = StatusCode.NOT_FOUND)

from django.views import generic
from django.views.generic import ListView

class CustomListView(ListView):
    #paginate_by = 2
    def get(self, request, *args, **kwargs):
      access_token = request.GET.get('access_token')

      
      error=[]

      if(Register.objects.filter(token_generated=access_token).exists()):
        pass
      else:
        error.append(
                  {
                    'status':401,
                    'message':"Access Token not valid"
                  }
            )
        return JsonResponse(error[0],safe=False)



      import sys
      print >> sys.stderr, access_token

      #vz_id = self.kwargs['vz_id']
         
      vz_id= Register.objects.filter(token_generated=access_token).values_list('vz_id',flat=True)[0]
      #tickets = Ticket.objects.filter(vz_id__in=contacts)
      print >> sys.stderr, vz_id
      
      obj=Ticket_create.objects.filter(vz_id=vz_id)
      from django.http import JsonResponse
     
      # objects=Connect.objects.filter(my_ticket__in=obj) 
      # print >> sys.stderr, objects

      print >> sys.stderr,"obj"
      print >> sys.stderr,obj

      import json

      def date_handler(obj):
        return obj.isoformat() if hasattr(obj, 'isoformat') else obj

      fields = []
      

      for t in obj:
        ticket_details=[]
        connections=[]
        print >> sys.stderr,t.ticket_id
        connect=Connect.objects.filter(my_ticket=t.ticket_id)
        # print >> sys.stderr,"connect"
        # print >> sys.stderr,connect


        for c in connect:
          if(Ticket_create.objects.filter(ticket_id=c.reffered_ticket).exists()):
            connections.append(
                      {
                       'connecter_details':Register.objects.filter(vz_id=c.connecter_vz_id).values('phone','photo','firstname', 'lastname', 'email','vz_id','industry','company','address_line_1','address_line_2','city','pin_code')[0], 
                       'reffered_phone_details':Register.objects.filter(phone=c.reffered_phone).values('phone','photo','firstname', 'lastname', 'email','vz_id','industry','company','address_line_1','address_line_2','city','pin_code')[0], 
                       'reffered_ticket_details':Ticket_create.objects.filter(ticket_id=c.reffered_ticket).values('vz_id','item_photo', 'question', 'item', 'description','date_created', 'date_validity','ticket_id')[0], 
                      }
                    )
          else:
            connections.append(
                      {
                       'connecter_details':Register.objects.filter(vz_id=c.connecter_vz_id).values('phone','photo','firstname', 'lastname', 'email','vz_id','industry','company','address_line_1','address_line_2','city','pin_code')[0], 
                       'reffered_phone_details':c.reffered_phone, 
                       'reffered_ticket_details':c.reffered_ticket,           
                      }
                    )
         
        print >> sys.stderr,"connections"
        print >> sys.stderr,connections

        

        fields.append(
                    {
                     'ticket_details':Ticket_create.objects.filter(ticket_id=t.ticket_id).values('vz_id','item_photo','question','item','description','date_created','date_validity','ticket_id')[0], 
                     'connections':connections
                    }
                  )

      response=[]
      count1=len(fields)

      fields = fields[::-1]

      
      from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
      # paginator = Paginator(response, self.paginate_by)
      paginator = Paginator(fields, 10)

      page = self.request.GET.get('page')

      print >> sys.stderr,"-----page------"
      print >> sys.stderr,page
      

      try:
          fields = paginator.page(page)
      except PageNotAnInteger:
          fields = paginator.page(1)
      except EmptyPage:
          fields = paginator.page(paginator.num_pages)


      print >> sys.stderr,"-----fields------"
      print >> sys.stderr,fields  

      response.append(
                {
                  'count':count1,
                  'response':list(fields)        
                }
        )


      # print >> sys.stderr,"-----------"
      # print >> sys.stderr,fields
      # print >> sys.stderr,"-----------"

         

      return JsonResponse(response[0],safe=False)


       

from django.contrib.auth.models import User
from history.serializers import UserSerializer
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
