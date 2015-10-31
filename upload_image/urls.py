from django.conf.urls import include
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from upload_image import views

urlpatterns = [
    url(r'^upload_image/$', views.Upload_imageList.as_view()),
    url(r'^upload_image/(?P<pk>[0-9]+)/$', views.Upload_imageDetail.as_view()),
    
	
]

urlpatterns = format_suffix_patterns(urlpatterns)

