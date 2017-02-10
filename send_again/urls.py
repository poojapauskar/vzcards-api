from django.conf.urls import include
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from send_again import views

urlpatterns = [
    url(r'^send_again/$', views.Send_againList.as_view()),
    url(r'^send_again/(?P<pk>[0-9]+)/$', views.Send_againDetail.as_view()),
    
	
]

urlpatterns = format_suffix_patterns(urlpatterns)

urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]