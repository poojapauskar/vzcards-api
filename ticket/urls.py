from django.conf.urls import include
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from ticket import views

urlpatterns = [
    url(r'^ticket/$', views.TicketList.as_view()),
    url(r'^ticket/(?P<pk>[0-9]+)/$', views.TicketDetail.as_view()),
    
	
]

urlpatterns = format_suffix_patterns(urlpatterns)

urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]