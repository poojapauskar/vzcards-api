from django.conf.urls import include
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from friends import views

urlpatterns = [
    url(r'^friends/$', views.FriendsList.as_view()),
    url(r'^friends/(?P<pk>[0-9]+)/$', views.FriendsDetail.as_view()),
    
	
]

urlpatterns = format_suffix_patterns(urlpatterns)

urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]