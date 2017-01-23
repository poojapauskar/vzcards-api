from user_register.models import User_register
# from login.serializers import LoginSerializer
from rest_framework import generics

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

class Delete_organizationList(generics.ListCreateAPIView):
 def get(self, request, *args, **kwargs):

  company=request.META.get('HTTP_COMPANY')

  details=[]

  User_register.objects.filter(company=company).update(is_organization="false")
  details.append(
            {
              'status':200,
              'message':'Organization Deleted',
            }
          )

  import sys
  from django.http import JsonResponse
  return JsonResponse(details[0],safe=False)