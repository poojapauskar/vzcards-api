from django.conf.urls import include
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from sync import views

urlpatterns = [
    url(r'^sync/$', views.SyncList.as_view()),
    url(r'^sync/(?P<pk>[0-9]+)/$', views.SyncDetail.as_view()),
    
	
]

urlpatterns = format_suffix_patterns(urlpatterns)

urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]