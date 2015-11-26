from django.conf.urls import include
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from user_register import views

urlpatterns = [
    url(r'^user_register/$', views.User_registerList.as_view()),
    url(r'^user_register/(?P<pk>[0-9]+)/$', views.User_registerDetail.as_view()),
    
	
]

urlpatterns = format_suffix_patterns(urlpatterns)
