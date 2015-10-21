from django.conf.urls import include
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from connect import views

urlpatterns = [
    url(r'^connect/$', views.ConnectList.as_view()),
    url(r'^connect/(?P<pk>[0-9]+)/$', views.ConnectDetail.as_view()),
    
	
]

urlpatterns = format_suffix_patterns(urlpatterns)

urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]