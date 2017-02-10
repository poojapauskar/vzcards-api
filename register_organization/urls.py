from django.conf.urls import include
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from register_organization import views
from register_organization.views import get_queryset

urlpatterns = [
    #url(r'^register_organization/$', views.Get_my_ticketsList.as_view()),
    url(r'^register_organization/$', get_queryset),
    #url(r'^get_list/(?P<vz_id>\d+)/$', views.Get_listDetail.as_view(), name='urlname'),

    
    
	
]

urlpatterns = format_suffix_patterns(urlpatterns)

urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]