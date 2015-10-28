from django.conf.urls import include
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from get_list import views

urlpatterns = [
    #url(r'^get_list/$', views.Get_listList.as_view()),
    url(r'^get_list/vz_id=(?P<vz_id>[A-Z0-9]+)/$', views.Get_listDetail.as_view()),
    #url(r'^get_list/(?P<vz_id>\d+)/$', views.Get_listDetail.as_view(), name='urlname'),

    
    
	
]

urlpatterns = format_suffix_patterns(urlpatterns)

urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]