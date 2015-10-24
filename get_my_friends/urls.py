from django.conf.urls import include
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from get_my_friends import views

urlpatterns = [
    url(r'^get_my_friends/$', views.Get_my_friendsList.as_view()),
    url(r'^get_my_friends/vz_id=(?P<vz_id>[A-Z0-9]+)/$', views.Get_my_friendsDetail.as_view()),
    #url(r'^get_my_friends/(?P<vz_id>\d+)/$', views.Get_my_friendsDetail.as_view(), name='urlname'),

    
    
	
]

urlpatterns = format_suffix_patterns(urlpatterns)

urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]