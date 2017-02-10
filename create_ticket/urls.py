from django.conf.urls import include
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from create_ticket import views

urlpatterns = [
    url(r'^create_ticket/$', views.Create_ticketList.as_view()),
    url(r'^create_ticket/(?P<pk>[0-9]+)/$', views.Create_ticketDetail.as_view()),
    
	
]

urlpatterns = format_suffix_patterns(urlpatterns)

urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]