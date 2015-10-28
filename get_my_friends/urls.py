from django.conf.urls import include
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from get_my_friends import views
from get_my_friends.views import get_queryset

urlpatterns = [
    #url(r'^get_my_friends/$', views.Get_my_friendsList.as_view()),
    url(r'^get_my_friends/$', get_queryset),
    #url(r'^get_my_friends/(?P<vz_id>\d+)/$', views.Get_my_friendsDetail.as_view(), name='urlname'),

    
    
	
]

urlpatterns = format_suffix_patterns(urlpatterns)

urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]