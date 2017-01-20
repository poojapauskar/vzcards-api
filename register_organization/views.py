from user_register.models import User_register
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

def get_queryset(request):

  import time

  list_of_phone_nos= request.META.get('HTTP_LIST_OF_PHONE_NOS')
  list_of_phone_nos= list_of_phone_nos.split(",")

  list_of_firstname= request.META.get('HTTP_LIST_OF_FIRSTNAME')
  list_of_firstname= list_of_firstname.split(",")

  list_of_lastname= request.META.get('HTTP_LIST_OF_LASTNAME')
  list_of_lastname= list_of_lastname.split(",")

  company=request.META.get('HTTP_COMPANY')

  i=0

  for obj in list_of_phone_nos:
   import sys
   print sys.stderr, obj
   print sys.stderr, list_of_firstname[i]
   print sys.stderr, list_of_lastname[i]
   print sys.stderr, company

   vz_id='VZ'+str(int(time.time()))

   if(User_register.objects.filter(phone=obj).exists()):
    User_register.objects.filter(phone=obj).update(company=company,is_organization="true")
   else: 
  	User_register.objects.create(vz_id=vz_id,reference_code=1,phone=obj,company=company,is_organization="true",firstname=list_of_firstname[i],lastname=list_of_lastname[i])
   
   i=i+1

  details=[]

  
  details.append(
            {
              'status':'true',
              'message':'Users registered in an organization',
            }
          )

  from django.http import JsonResponse
  #return JsonResponse(dict(objects=list(objects)))
  return JsonResponse((list(details)),safe=False)

