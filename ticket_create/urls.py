from django.conf.urls import include
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from ticket_create import views

urlpatterns = [
    url(r'^ticket_create/$', views.Ticket_createList.as_view()),
    url(r'^ticket_create/(?P<pk>[0-9]+)/$', views.Ticket_createDetail.as_view()),
    
	
]

urlpatterns = format_suffix_patterns(urlpatterns)

urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]