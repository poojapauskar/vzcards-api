from django.conf.urls import include
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from remove_ticket import views

urlpatterns = [
    #url(r'^my_profile/$', views.My_profileList.as_view()),
    url(r'^remove_ticket/?ticket_id=(?P<ticket_id>(\w+))/$', views.Remove_ticketDetail.as_view()),
    #url(r'^get_list/(?P<vz_id>\d+)/$', views.Get_listDetail.as_view(), name='urlname'),

    
    
	
]

urlpatterns = format_suffix_patterns(urlpatterns)

urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]