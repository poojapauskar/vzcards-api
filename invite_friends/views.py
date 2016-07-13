from connect.models import Connect
from user_register.models import User_register
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

      from django.http import JsonResponse
      
      if(User_register.objects.filter(token_generated=access_token).exists()):
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

      import sys
      print sys.stderr, request.META.get('HTTP_SENDER')
      print sys.stderr, request.META.get('HTTP_RECEIVER')
      print sys.stderr, request.META.get('HTTP_PHONE')

      if (str(request.META.get('HTTP_PHONE'))[:2] == '91'):
        print sys.stderr, "Indian Numbers"
        from pprint import pprint
        import requests
        from django.conf import settings

        sid = 'bitjini2'
        token = 'e064d27250bdd098a3aca1822adf24e1039d219a'

        def send_message(sid, token, sms_from, sms_to, sms_body):
        	return requests.post('https://twilix.exotel.in/v1/Accounts/{sid}/Sms/send.json'.format(sid=sid),
        		auth=(sid, token),
        		data={
        		'From': sms_from,
        		'To': sms_to,
        		'Body': sms_body
        		})
        r = send_message(sid, token,
        	sms_from='08030752644',
        	sms_to=request.META.get('HTTP_PHONE'),
        	sms_body='Hi '+request.META.get('HTTP_RECEIVER')+', '+request.META.get('HTTP_SENDER')+' has invited you to VzCards. Please click on the link to download the app https://itunes.apple.com/in/app/beautiful-photos/id1111832526?mt=8.')
        print r.status_code
        pprint(r.json())
	  ##--------------------------------------------
      else:
        print sys.stderr, "International Numbers"
        import urllib
        import urllib2

        params = {
        	'api_key': '24def3ee',
        	'api_secret': '865357d5',
        	'to': request.data['phone'],
        	'from': 'NEXMO',
        	'text': 'Hi '+request.META.get('HTTP_RECEIVER')+', '+request.META.get('HTTP_SENDER')+' has invited you to VzCards. Please click on the link to download the app https://itunes.apple.com/in/app/beautiful-photos/id1111832526?mt=8.'
        }

        url = 'https://rest.nexmo.com/sms/json?' + urllib.urlencode(params)

        request = urllib2.Request(url)
        request.add_header('Accept', 'application/json')
        response = urllib2.urlopen(request)

        #-----------------------------

	  	
  
      response=[]
      response.append(
                {
                  'status':200,       
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

			